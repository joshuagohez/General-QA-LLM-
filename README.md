# Generative Question-Answering (GQA) Bot

This bot allows you to chat with an external uploaded PDF file using GPT functionalities.

## Description
Did up this PDF QA bot demo to better understand the arena of LLM and its application abilities as my first project as an intern in CDG. In summary this application utilises the langchain framework built around LLMs with panel for a quick frontend dashboard generation.

The application splits the document into smaller chunks and employs OpenAI embeddings to measure the relatedness of text strings. DO NOTE this costs $. Set up billing at [OpenAI](https://platform.openai.com/account). Requests are billed based on the number of tokens in the input sent. It is acknowledged that the OpenAI embeddings are considered poor in the hugging face community hence the option to use improved embeddings to reduce hallucinations and improve content quality is open.

The option to customise the chaintype for the QA is open too but it is generally recommended to use "map_reduce" to ensure the the chunks are fed in batches instead of passing the whole pdf chunk in when using "stuff" chain type, preventing crash of the LLM. KNN algorithm is then incorporated to generate the most appropraite response from the extracted chunks compared against the question vector before passing it back to the GPT.

The LLM used is OpenAI's GPT-3.5. The option to feed another LLM is open.

The memory vectorstore used is pinecone for long-term memory. Ensure the right pinecone API key, environment and index_name is inputted before proceeding else the option to switch out to other long-term vectorstores or short-term vectorstores i.e Chroma is open (and easier).

The output of each run is stored locally and the model will refine and generate each response based on the history. Depending on the `k` chunks defined, the same k number of sources will be acknowledged below the result.

## Demo Screenshots

<img width="669" alt="Screenshot 2023-05-04 at 2 29 58 PM" src="https://user-images.githubusercontent.com/96434745/236127424-30805ed3-9cd4-4563-9f38-a583b5c13d71.png">
<img width="667" alt="Screenshot 2023-05-04 at 2 30 22 PM" src="https://user-images.githubusercontent.com/96434745/236127430-8859043e-96c0-4d84-a2ab-7ff3b77c84cf.png">

## Getting Started

### Dependencies

* Ensure LTS python version is installed

### Installing

`pip3 install langchain openai chromadb pypdf tiktoken panel notebook pinecone-client`
* Ensure the right embeddings, vectorstores and LLMs are used with the appropriate API keys and relevant information are feed into the code chunk

### Executing program

* How to run the program
```
panel serve qaApp.py
```
open `http://localhost:5006/qaApp` in browser once successfully run in local

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

* [Project ideation](https://www.youtube.com/watch?v=DXmiJKrQIvg&t=620s)
* [Langchain documentation](https://python.langchain.com/en/latest/index.html)
* [Panel documentation](https://panel.holoviz.org/)
* [OpenAI API documentation](https://platform.openai.com/docs/introduction)
