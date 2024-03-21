import gradio as gr

#TODO Looks and Logic
def getLayoutStart() -> gr.Blocks:
    with gr.Blocks() as layout:
        gr.Markdown("""# Learning Finish""")
        gr.Markdown("""The assisted finnish-learning experience""")
        button = gr.Button(value= "New Game", link="/rules")
    layout.queue()
    return layout