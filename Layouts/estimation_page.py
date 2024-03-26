import gradio as gr
import Layouts.Style.style as st
import Data.data as data

#TODO: adjust styling for table-display
#css for styling
style = st.GetStyleEstimationPage()

#establish database connection
db = data.createDB()
cursor = db.cursor()

#retrieve cases from database
#TODO: retrieve actual estimation
numberofcases = 5

#layout for estimation-page
def getLayoutEstimation() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(), css=style) as layout:

        #header and sub-header
        gr.Markdown("""# Estimation """)
        gr.Markdown(""" Estimation of cards you have chosen: 
                    """)
        
        #dataframe/table for case display
        gr.Dataframe(
            value = data.retrieveEstimation(cursor, numberofcases), #TODO: save data.retrieve... as a variable, like in tests_page.py
            headers = ["nominative", "inessive"],
            datatype = ["str", "str"],
            row_count = numberofcases,
            col_count = (2, "fixed"),
        ),

        #continue and go-back button
        with gr.Row():
            bbutton = gr.Button(value="go back", link="/score",
                                elem_id="go_back_button")
            cbutton = gr.Button(value="see recommendations",
                                link="/recommendations",
                                elem_id="continue_button")
            
    layout.queue()
    return layout
