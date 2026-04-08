import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from fastapi import FastAPI
from env.env import CodeReviewEnv
from env.tasks import EasyTask

app = FastAPI()

# THIS is what checker calls
@app.post("/")
def reset():
    env = CodeReviewEnv(EasyTask())
    obs = env.reset()

    return {
        "title": obs["title"],
        "code": obs["code"],
        "goal": obs["goal"]
    }

@app.get("/")
def root():
    return {"message": "Code Review Env Running"}
