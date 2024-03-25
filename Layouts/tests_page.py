import gradio as gr
import Layouts.Style.style as st
import Data.data as data


# Establish database connection
db = data.createDB()
cursor = db.cursor()


# Retrieve Cases from database 
index_test_cases = 0
numberoftests = 5
test_cases = data.retrieveRandomCase(cursor, numberoftests)

#TODO Looks and Logic
style = st.GetStyleTestsPage()

#TODO: Fix global variables

def getLayoutTests() -> gr.Blocks:
    
    with gr.Blocks(theme=gr.themes.Soft(), css=style) as layout:
        def submit(answer):
            global test_cases
            global index_test_cases
            index_test_cases += 1  
            if (index_test_cases == numberoftests): 
                index_test_cases = 0
                return {continue_button: gr.Button(visible=True), 
                       row: gr.Row(visible = False)
                       }
            return {output: gr.Textbox(value = test_cases[index_test_cases][0])}
        gr.Markdown("""# Tests 
                    """)
        continue_button = gr.Button(value="continue", link="/score",
                           elem_id="continue_button", visible=False)
        with gr.Row(visible=True) as row:
            with gr.Column(1):
                output = gr.Textbox(label="question", value=test_cases[index_test_cases][0], elem_id="caseBox")
            gr.Markdown(value="→")
            with gr.Column(1):
                input = gr.Textbox(label="answer", elem_id="answerBox")
                submit_btn = gr.Button("Submit", elem_id="submit_btn")
                submit_btn.click(fn=submit, inputs=input, outputs=[output, continue_button, row])
    layout.queue()
    return layout

#TODO add functionality
