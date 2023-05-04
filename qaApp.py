import os
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Pinecone
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import widget
import panel as p
import pinecone
import getpass

p.extension('texteditor', template="bootstrap", sizing_mode='stretch_width')
p.state.template.param.update(
    main_max_width="690px",
    header_background="F08080",
)

history = [] 

# QA function definition
def qa(file, query, chain_type, k):
    loader = PyPDFLoader(file)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    pinecone.init(
        api_key="INSERT PINECONE API KEY",  
        environment="INSERT PINECONE ENV" 
    )

    index_name = "INSERT NAME OF PINECONE INDEX"

    db = Pinecone.from_documents(docs, embeddings, index_name=index_name)

    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": k})

    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        chain_type=chain_type,
        retriever=retriever,
        return_source_documents=True
    )
    result = qa({"query": query})
    print(result["result"])
    return result

def qa_result(_):
    os.environ["OPENAI_API_KEY"] = widget.openaikey.value

    if widget.file_input.value is not None:
        widget.file_input.save("./temp.pdf")

        prompt_text = widget.prompt.value
        if prompt_text:
            result = qa(file="./temp.pdf", 
                        query=prompt_text, 
                        chain_type=widget.select_chain_type.value, 
                        k=widget.select_k.value)
            
            history.extend([
                p.Row(
                    p.panel("\U0001f468\u200D\U0001f4bb", width=10),
                    prompt_text,
                    width=600
                ),
                p.Row(
                    p.panel("\U0001F916", width=10),
                    p.Column(
                        result["result"],
                        "Relevant source text:",
                        p.pane.Markdown("\n--------------------------------------------------------------------\n"
                            .join(doc.page_content for doc in result["source_documents"]))
                    )
                )
            ])
    return p.Column(*history, margin=15, width=575, min_height=400)

qa_interactive = p.panel(
    p.bind(qa_result, widget.run_button),
    loading_indicator=True
)

output = p.WidgetBox("Output will be generated here:",
                     qa_interactive,
                     width=630,
                     scroll=True)

if os.path.exists("./temp.pdf"):
    pdf_panel = p.pane.PDF("./temp.pdf", width=630, height=870)
else:
    pdf_panel = p.pane.PDF("http://www.africau.edu/images/default/sample.pdf", width=630, height=870, visible=False)



p.Column(
    p.pane.Markdown("""
    ## Generative Question Answering with your PDF file
    1) Upload a PDF. 
    2) Enter OpenAI API key. 
    3) Type a question and click "Run"
    """
    ),
    p.Row(widget.file_input, widget.openaikey),
    output,
    widget.widgets,
    pdf_panel
).servable()

#This costs $. Set up billing at [OpenAI](https://platform.openai.com/account). 