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

#get new run id -- For every new run please restart the application
#otherwise the won't be updated
runId = data.getlastrun(cursor) + 1

# This is for checking if the user is repeating the test
FirstRound = True

#css for styling
style = st.GetStyleTestsPage()

#TODO: Fix global variables

def getLayoutTests() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(), css=style) as layout:

        #function for submit_btn.click
        def submit(answer):
            global test_cases
            global index_test_cases
            global FirstRound

            #Logic for Database, Inserting User Input
            if (FirstRound):
                word_id = test_cases.iloc[index_test_cases]['id']
                position = index_test_cases + 1
                data.InsertIntoRunsFirstRound(cursor, runId, position, word_id, answer)
                db.commit()
            else:
                word_id = test_cases.iloc[index_test_cases]['id']
                position = index_test_cases + 1
                data.InsertIntoRunsSecondRound(cursor, runId, position, word_id, answer)
                db.commit()
            #increasing the index with each button-click
            index_test_cases += 1  
            position += 1


            #when the index reaches the end of the test-cases, the index is set to 0 (in case the tests are redone), the visibility
            #of the test-UI is turned off and the visibility of the the continue button is turned on
            if (index_test_cases == number_of_tests): 
                FirstRound = False
                index_test_cases = 0    
                position = 1
                return {continue_button: gr.Button(visible=True), 
                       row: gr.Row(visible = False)}
            
            #display next case
            return {output: gr.Textbox(value = test_cases.iloc[index_test_cases]['nominative'])}
        
        #header
        gr.Markdown("""# Tests""")
        
        #(hidden) continue button
        continue_button = gr.Button(value="continue", link="/score",
                           elem_id="continue_button", visible=False)
        
        #test-UI with submit-button
        with gr.Row(visible=True) as row:
            with gr.Column(1):
                output = gr.Textbox(label="question", value=test_cases.iloc[index_test_cases]['nominative'], elem_id="caseBox")
            gr.Markdown(value="→", elem_id="arrow")
            with gr.Column(1):
                input = gr.Textbox(label="answer", elem_id="answerBox")
                submit_btn = gr.Button("Submit", elem_id="submit_btn")
                submit_btn.click(fn=submit, inputs=input, outputs=[output, continue_button, row])

    layout.queue()
    return layout

#TODO add functionality
#TODO send user input to DB
