import gradio as gr
import Layouts.Style.style as st
import Data.data as data

# TODO Looks and Logic
style = st.GetStyleEstimationPage()
db = data.createDB()
cursor = db.cursor()
numberofcases = 5

def getLayoutEstimation() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(), css=style) as layout:
        gr.Markdown("""# Estimation """)
        gr.Markdown(""" Estimation of cards you have chosen: 
                    """)
        gr.Dataframe(
            value = data.retrieveEstimation(cursor, numberofcases),
            headers = ["nominative", "inessive"],
            datatype = ["str", "str"],
            row_count = numberofcases,
            col_count = (2, "fixed"),
        ),

        with gr.Row():
            bbutton = gr.Button(value="go back", link="/score",
                                elem_id="go_back_button")
            cbutton = gr.Button(value="see recommendations",
                                link="/recommendations",
                                elem_id="continue_button")
    layout.queue()
    return layout
