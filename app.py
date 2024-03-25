from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import gradio as gr
from Layouts import *

app = FastAPI()


# def app() -> FastAPI:
#    pass

start_screen = start_page.getLayoutStart()
rule_screen = rules_page.getLayoutRules()
tests_screen = tests_page.getLayoutTests()
score_screen = score_page.getLayoutScore()
esti_screen = estimation_page.getLayoutEstimation()
recomm_screen = recommendation_page.getLayoutRecommendation()
gr.mount_gradio_app(app=app, blocks=start_screen, path="/start")
gr.mount_gradio_app(app=app, blocks=rule_screen, path="/rules")
gr.mount_gradio_app(app=app, blocks=tests_screen, path="/tests")
gr.mount_gradio_app(app=app, blocks=score_screen, path="/score")
gr.mount_gradio_app(app=app, blocks=esti_screen, path="/estimation")
gr.mount_gradio_app(app=app, blocks=recomm_screen, path="/recommendations")


@app.get("/")
def redirectToStart():
    response = RedirectResponse(url='/start')
    return response


# Maybe into function
