import gradio as gr
import Layouts.Style.style as st

#css for styling
style = st.GetStyleRulesPage()

#layout for rules-page
def getLayoutRules() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(), css=style) as layout:

        #header and sub-header
        gr.Markdown("""# Rules """)
        gr.Markdown(""" In the following, you will be presented with X finnish words in theire nominative form.
                   You will have to enter the inessive form of the words.
                   """)
        gr.Markdown(""" You can choose Y random cards with examples in order to pratice the
                   transformation of the words.""")
        gr.Markdown(""" At the end you will be presented with your personal score.
                   """)
        gr.Markdown(""" After this, the AI will show you the cards it thinks you've seen and recommend
                   new/other cards for practice and to reach a higher score.""")
        gr.Markdown(""" Press the button below whenever you're ready to begin!
                    """)
        
        #continue button
        button = gr.Button(value= "Start Testing!", link="/tests",
                           elem_id="continue_button")
    layout.queue()
    return layout