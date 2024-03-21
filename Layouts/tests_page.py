import gradio as gr

#TODO Looks and Logic
def getLayoutTests() -> gr.Blocks:
    with gr.Blocks() as layout:
        gr.Markdown("""# Tests 
                    """) #TODO add test count/progress
    #TODO add submit button
        button = gr.Button(value="continue", link="/score") #Only for path-testing!
    layout.queue()
    return layout