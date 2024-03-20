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
    layout.queue()
    return layout


#TODO add remaining paths
start_screen = getLayoutStart()
rule_screen = getLayoutRules()
tests_screen = getLayoutTests()
gr.mount_gradio_app(app=app, blocks=start_screen, path="/start")
gr.mount_gradio_app(app=app, blocks=rule_screen, path="/rules")
gr.mount_gradio_app(app=app, blocks=tests_screen, path="/tests")
# Maybe into function
