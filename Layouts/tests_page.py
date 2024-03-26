import gradio as gr
import Layouts.Style.style as st
import Data.data as data

#establish database connection
db = data.createDB()
cursor = db.cursor()

#retrieve Cases from database 
index_test_cases = 0
number_of_tests = 5
test_cases = data.retrieveRandomCase(cursor, number_of_tests)

#css for styling
style = st.GetStyleTestsPage()

#TODO: fix global variables
#layout for tests-page
def getLayoutTests() -> gr.Blocks:
    
    with gr.Blocks(theme=gr.themes.Soft(), css=style) as layout:

        #function for submit_btn.click
        def submit(answer):
            global test_cases
            global index_test_cases

            #increasing the index with each button-click
            index_test_cases += 1  

            #when the index reaches the end of the test-cases, the index is set to 0 (in case the tests are redone), the visibility
            #of the test-UI is turned off and the visibility of the the continue button is turned on
            if (index_test_cases == number_of_tests): 
                index_test_cases = 0    
                return {continue_button: gr.Button(visible=True), 
                       row: gr.Row(visible = False)
                       }
            
            #display next case
            return {output: gr.Textbox(value = test_cases[index_test_cases][0])}
        
        #header
        gr.Markdown("""# Tests 
                    """)
        
        #(hidden) continue button
        continue_button = gr.Button(value="continue", link="/score",
                           elem_id="continue_button", visible=False)
        
        #test-UI with submit-button
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
#TODO send user input to DB
