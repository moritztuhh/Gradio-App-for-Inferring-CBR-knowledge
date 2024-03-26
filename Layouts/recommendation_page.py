import gradio as gr
import Layouts.Style.style as st
import Data.data as data

#TODO: adjust styling for table-display
#css for styling
style = st.GetStyleRecommendationPage()

#establish database connection
db = data.createDB()
cursor = db.cursor()

#retrieve Cases from database
#TODO: retrieve actual recommendation
numberofcases = 5

#layout for reccomendation-page
def getLayoutRecommendation() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(),css=style) as layout:
        
        #header
        gr.Markdown("""# Recommendations
                    """)
        
        #dataframe/table for case display
        gr.Dataframe(
            value = data.retrieveRecommendations(cursor, numberofcases),  #TODO: save data.retrieve... as a variable, like in tests_page.py
            headers = ["nominative", "inessive"],
            datatype = ["str", "str"],
            row_count = numberofcases,
            col_count = (2, "fixed"),
        ), #TODO what if no recommendations?

        #quit and redo-tests button
        with gr.Row():
            bbutton = gr.Button(value="quit", link="/start",
                                elem_id="go_back_button") #TODO start a new run
            cbutton = gr.Button(value="redo tests", link="/tests",
                                elem_id="continue_button")
            
    layout.queue()
    return layout