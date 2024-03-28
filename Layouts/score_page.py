import gradio as gr
import Layouts.Style.style as st
import Data.data as data

#establish database connection
db = data.createDB()
cursor = db.cursor()

#TODO function that determines second round 
FirstRun = True 

#css for styling
style = st.GetStyleScorePage()

#layout for score-page
def getLayoutScore() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(),css=style) as layout:
        score = data.CalculateFirstScoreForRun(cursor) if FirstRun else data.CalculateSecondScoreForRun(cursor) 
        #header and sub-header
        gr.Markdown("""# Score """)
        gr.Markdown(f"your score is: {score}")
        
        #TODO: get infos from DB
        #TODO: calculate score
        #TODO:display score
        
        #continue button
        button = gr.Button(value="continue", link="/estimation",
                           elem_id="continue_button")
        
    layout.queue()
    return layout