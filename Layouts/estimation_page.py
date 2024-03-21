import gradio as gr
import Layouts.Style.style as st

# TODO Looks and Logic
style = st.GetStyleEstimationPage()

def getLayoutEstimation() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(), css=style) as layout:
        gr.Markdown("""# Estimation """)
        gr.Markdown(""" Estimation of cards you have chosen: 
                    """)
        # TODO add dynamic space for case-display (The number of cases may vary!!!)

        with gr.Row():
            bbutton = gr.Button(value="go back", link="/score",
                                elem_id="go_back_button")
            cbutton = gr.Button(value="see recommendations",
                                link="/recommendations",
                                elem_id="continue_button")
    layout.queue()
    return layout
