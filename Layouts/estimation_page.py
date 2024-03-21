import gradio as gr

# TODO Looks and Logic


def getLayoutEstimation() -> gr.Blocks:
    with gr.Blocks() as layout:
        gr.Markdown("""# Estimation of cards you have chosen: 
                    """)
        # TODO add dynamic space for case-display (The number of cases may vary!!!)

        with gr.Row():
            bbutton = gr.Button(value="go back", link="/score")
            cbutton = gr.Button(value="see recommendations",
                                link="/recommendations")
    layout.queue()
    return layout
