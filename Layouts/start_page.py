import gradio as gr
import Layouts.Style.style as st

# TODO Looks


def getLayoutStart() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(), css=st.GetStyleStartPage()) as layout:
        gr.Markdown("""# Learning Finish""")
        gr.Markdown("""The assisted finnish-learning experience""")
        button = gr.Button(value="New Game", link="/rules",
                           elem_id="start_button")
    layout.queue()
    return layout
