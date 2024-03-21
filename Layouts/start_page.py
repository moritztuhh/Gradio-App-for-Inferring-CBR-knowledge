import gradio as gr
from Style.style import GetStyleStartPage

style = GetStyleStartPage()

# TODO Looks and Logic


def getLayoutStart() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(), css=style) as layout:
        gr.Markdown("""# Learning Finish""")
        gr.Markdown("""The assisted finnish-learning experience""")
        button = gr.Button(value="New Game", link="/rules")
    layout.queue()
    return layout
