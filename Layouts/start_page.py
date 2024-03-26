import gradio as gr
import Layouts.Style.style as st

#css for styling
style = st.GetStyleStartPage()

#layout for start-page
def getLayoutStart() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(), css=style) as layout:

        #header and sub-header
        gr.Markdown("""# Learning Finnish""")
        gr.Markdown("""The assisted finnish-learning experience""")

        #continue/start button
        button = gr.Button(value="New Game", link="/rules",
                           elem_id="continue_button")
        
    layout.queue()
    return layout
