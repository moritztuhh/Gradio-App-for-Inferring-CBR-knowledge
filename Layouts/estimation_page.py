import gradio as gr
import Layouts.Style.style as st

# TODO Looks and Logic
style = st.GetStyleEstimationPage()

def getLayoutEstimation() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(), css=style) as layout:
        gr.Markdown("""# Estimation of cards you have chosen: 
                    """)
        # TODO add dynamic space for case-display (The number of cases may vary!!!)

        with gr.Row():
            bbutton = gr.Button(value="go back", link="/score")
            cbutton = gr.Button(value="see recommendations",
                                link="/recommendations")
    layout.queue()
    return layout
