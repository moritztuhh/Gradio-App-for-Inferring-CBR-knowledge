from fastapi import FastAPI
import gradio as gr

app = FastAPI()


# def app() -> FastAPI:
#    pass


# def Btn1_RerouteToLayout2():
#     # TODO: Find a way to reroute on button press
#     pass

# TODO: Make page look good (center markdown)
def getLayoutStart() -> gr.Blocks:
    with gr.Blocks() as layout:
        gr.Markdown("""# Learning Finish""")
        gr.Markdown("""The assisted finnish learning experience""")
        button = gr.Button()
    layout.queue()
    return layout


# TODO: Logic and Look
def getLayout2() -> gr.Blocks:
    with gr.Blocks() as layout:
        gr.Markdown(""" In the following, you will be presented with X finnish words in theire nominative form.
                   You will have to enter the inessive form of the words.
                   """)
        gr.Markdown(""" You can choose Y random cards with examples in order to pratice the
                   transformation of the words.""")
        gr.Markdown(""" At the end you will be presented with your personal score.
                   """)
        gr.Markdown(""" After this, the AI will shpw you the cards it thinks you've seen and recommend
                   new/other cards for the practice and to reach a higher score!""")
    layout.queue()
    return layout


block1 = getLayoutStart()
block2 = getLayout2()
gr.mount_gradio_app(app=app, blocks=block1, path="/block1")
gr.mount_gradio_app(app=app, blocks=block2, path="/block2")

# Maybe into function
