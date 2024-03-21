import gradio as gr

#TODO Looks and Logic
def getLayoutRecommendation() -> gr.Blocks:
    with gr.Blocks() as layout:
        gr.Markdown("""# Recommendations
                    """)
        #TODO add dynamic space for case-display (The number of cases may vary!!!)
        #TODO what if no recommendations?
        with gr.Row():
            bbutton = gr.Button(value="quit", link="/start") #TODO delete cache of "last" player
            cbutton = gr.Button(value="redo tests", link="/tests") #does redoing the tests even make sense?
    layout.queue()
    return layout