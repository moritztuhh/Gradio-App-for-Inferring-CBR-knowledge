import gradio as gr

#TODO Looks and Logic
def getLayoutScore() -> gr.Blocks:
    with gr.Blocks() as layout:
        gr.Markdown("""# your score is: 
                    """)
        button = gr.Button(value="continue", link="/estimation")
    layout.queue()
    return layout