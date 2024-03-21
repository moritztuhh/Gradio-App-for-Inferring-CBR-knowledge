import gradio as gr
import Layouts.Style.style as st

#TODO Looks and Logic
style= st.GetStyleScorePage()

def getLayoutScore() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(),css=style) as layout:
        gr.Markdown("""# Score """)
        gr.Markdown(""" your score is: 
                    """)
        button = gr.Button(value="continue", link="/estimation",
                           elem_id="continue_button")
    layout.queue()
    return layout