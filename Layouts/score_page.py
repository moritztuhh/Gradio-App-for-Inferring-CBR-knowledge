import gradio as gr
import Layouts.Style.style as st

#TODO adjust styling for score-display
#css for styling
style = st.GetStyleScorePage()

#layout for score-page
def getLayoutScore() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(),css=style) as layout:
        
        #header and sub-header
        gr.Markdown("""# Score """)
        gr.Markdown(""" your score is: 
                    """)
        
        #TODO: get infos from DB
        #TODO: calculate score
        #TODO:display score
        
        #continue button
        button = gr.Button(value="continue", link="/estimation",
                           elem_id="continue_button")
        
    layout.queue()
    return layout