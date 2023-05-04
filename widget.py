import panel as p

# panel widgets
file_input = p.widgets.FileInput(width=300)

openaikey = p.widgets.PasswordInput(
    value="",
    placeholder="Enter your OpenAI API key here:",
    width=300
)

prompt = p.widgets.TextEditor(
    value="",
    placeholder="Enter your questions:",
    height=160,
    toolbar=False
)

run_button = p.widgets.Button(
    name="Run"
)

select_k = p.widgets.IntSlider(
    name="Number of relevant chunks",
    start=1,
    end=5,
    step=1,
    value=3
)

select_chain_type = p.widgets.RadioButtonGroup(
    name="Chain Type",
    options=["stuff", "map_reduce", "refine", "map_rerank"]
)

widgets = p.Row(
    p.Column(prompt, run_button, margin=5),
    p.Card(
        "Chain Type:",
        p.Column(select_chain_type, select_k),
        title="Advanced settings",
        margin=10
    ), width=600
)