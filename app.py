from fastapi import FastAPI
import gradio as gr


def app() -> FastAPI:
    pass


def getLayoutStart() -> gr.Blocks:
    with gr.Blocks() as layout:
        gr.Markdown("""# Learning Finish""")
        gr.Markdown("""The assisted finnish learning experience""")
        button = gr.Button()
        button.click(fn=image_generator,
                     inputs=gr.Textbox(), outputs=gr.Image())
    layout.queue()
    return layout


def getLayout2() -> gr.Blocks:
    with gr.Blocks() as layout:
        checkbox = gr.Checkbox()
        # button.click(fn=image_generator, inputs=gr.Textbox(), outputs=gr.Image())
    layout.queue()
    return layout


# Maybe into function
app = FastAPI()
block1 = getLayoutStart()
block2 = getLayout2()
gr.mount_gradio_app(app=app, blocks=block1, path="/block1")
gr.mount_gradio_app(app=app, blocks=block2, path="/block2")
