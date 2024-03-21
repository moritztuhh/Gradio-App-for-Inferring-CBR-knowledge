from fastapi import FastAPI
import gradio as gr

app = FastAPI()


# def app() -> FastAPI:
#    pass


# def Btn1_RerouteToLayout2():
#     # TODO: Find a way to reroute on button press
#     pass

# TODO styling: center title/text, adjust sizes
def getLayoutStart() -> gr.Blocks:
    with gr.Blocks() as layout:
        gr.Markdown("""# Learning Finish""")
        gr.Markdown("""The assisted finnish-learning experience""")
        button = gr.Button(value= "New Game", link="/rules")
    layout.queue()
    return layout

# TODO: Logic and Look
def getLayoutRules() -> gr.Blocks:
    with gr.Blocks() as layout:
        gr.Markdown(""" In the following, you will be presented with X finnish words in theire nominative form.
                   You will have to enter the inessive form of the words.
                   """)
        gr.Markdown(""" You can choose Y random cards with examples in order to pratice the
                   transformation of the words.""")
        gr.Markdown(""" At the end you will be presented with your personal score.
                   """)
        gr.Markdown(""" After this, the AI will show you the cards it thinks you've seen and recommend
                   new/other cards for the practice and to reach a higher score.""")
        gr.Markdown(""" Press the button below whenever you're ready to begin!
                    """)
        button = gr.Button(value= "Start Testing!", link="/tests")
    layout.queue()
    return layout

# TODO: Logic and Look
def getLayoutTests() -> gr.Blocks:
    with gr.Blocks() as layout:
        gr.Markdown("""# Tests 
                    """) #TODO add test count/progress
    #TODO add submit button
        button = gr.Button(value="continue", link="/score") #Only for path-testing!
    layout.queue()
    return layout

#TODO: Logic and Look
def getLayoutScore() -> gr.Blocks:
    with gr.Blocks() as layout:
        gr.Markdown("""# your score is: 
                    """)
        button = gr.Button(value="continue", link="/estimation")
    layout.queue()
    return layout

#TODO: Logic and Look
def getLayoutEstimation() -> gr.Blocks:
    with gr.Blocks() as layout:
        gr.Markdown("""# Estimated cards you have chosen: 
                    """)
        #TODO add dynamic space for case-display (The number of cases may vary!!!)
    
        with gr.Row():
            bbutton = gr.Button(value="go back", link="/score")
            cbutton = gr.Button(value="see recommendations", link="/recommendations")
    layout.queue()
    return layout

#TODO: Look and Logic
def getLayoutRecommendation() -> gr.Blocks:
    with gr.Blocks() as layout:
        gr.Markdown("""# Recommendations
                    """)
        #TODO add dynamic space for case-display (The number of cases may vary!!!)
        #TODO what if no recommendations?
        with gr.Row():
            bbutton = gr.Button(value="quit", link="/start") #TODO delete cache of "last" player
            cbutton = gr.Button(value="redo tests", link="/tests") #does redoing the tests even make sense?
    layout.queue()
    return layout

#TODO add remaining paths
start_screen = getLayoutStart()
rule_screen = getLayoutRules()
tests_screen = getLayoutTests()
score_screen = getLayoutScore()
esti_screen = getLayoutEstimation()
recomm_screen = getLayoutRecommendation()
gr.mount_gradio_app(app=app, blocks=start_screen, path="/start")
gr.mount_gradio_app(app=app, blocks=rule_screen, path="/rules")
gr.mount_gradio_app(app=app, blocks=tests_screen, path="/tests")
gr.mount_gradio_app(app=app, blocks=score_screen, path="/score")
gr.mount_gradio_app(app=app, blocks=esti_screen, path="/estimation")
gr.mount_gradio_app(app=app, blocks=recomm_screen, path="/recommendations")
# Maybe into function
