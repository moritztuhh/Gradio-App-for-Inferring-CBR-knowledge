import gradio as gr
import Layouts.Style.style as st
import Data.data as data

#TODO Looks and Logic
style =st.GetStyleRecommendationPage()

db = data.createDB()
cursor = db.cursor()
numberofcases = 5

def getLayoutRecommendation() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(),css=style) as layout:
        gr.Markdown("""# Recommendations
                    """)
        gr.Dataframe(
            value = data.retrieveRecommendations(cursor, numberofcases),
            headers = ["nominative", "inessive"],
            datatype = ["str", "str"],
            row_count = numberofcases,
            col_count = (2, "fixed"),
        ),
        #TODO what if no recommendations?
        with gr.Row():
            bbutton = gr.Button(value="quit", link="/start",
                                elem_id="go_back_button") #TODO delete cache of "last" player
            cbutton = gr.Button(value="redo tests", link="/tests",
                                elem_id="continue_button") 
    layout.queue()
    return layout