import gradio as gr
import Layouts.Style.style as st

#TODO Looks and Logic
style = st.GetStyleTestsPage()

def getLayoutTests() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(), css=style) as layout:
        gr.Markdown("""# Tests 
                    """) #TODO add test count/progress
    #TODO add submit button
        button = gr.Button(value="continue", link="/score") #Only for path-testing!
    layout.queue()
    return layout