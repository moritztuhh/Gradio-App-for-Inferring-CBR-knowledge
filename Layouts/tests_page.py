import gradio as gr
import Layouts.Style.style as st

test_cases = [['baum', 'bäume'], ['Ast', 'Äste'],['Maus', 'Mäuse'],['Haus', 'Häuser'], ['PLEASE CONTINUE', 'PLEASE CONTINUE']]
n_tests = 4
index_test_cases = 0

#TODO Looks and Logic
style = st.GetStyleTestsPage()

def getLayoutTests() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(), css=style) as layout:
        gr.Markdown("""# Tests 
                    """)
        with gr.Row():
            with gr.Column(1):
                output = gr.Textbox(label="question", value=test_cases[index_test_cases][0], elem_id="caseBox")
            gr.Markdown(value="→")
            with gr.Column(1):
                input = gr.Textbox(label="answer", elem_id="answerBox")
                submit_btn = gr.Button("Submit", elem_id="submit_btn")
                submit_btn.click(fn=sendAnswer, inputs=input, outputs=output)
        button = gr.Button(value="continue", link="/score",
                           elem_id="continue_button")
    layout.queue()
    return layout

#TODO add functionality
def sendAnswer(answer):
    global index_test_cases
    global test_cases
    index_test_cases += 1
    return test_cases[index_test_cases][0]
