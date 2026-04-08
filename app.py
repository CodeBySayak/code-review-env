from fastapi import FastAPI
from env.env import CodeReviewEnv
from env.tasks import EasyTask

app = FastAPI()

@app.post("/")
def reset():
    env = CodeReviewEnv(EasyTask())
    obs = env.reset()

    return {
        "title": obs["title"],
        "code": obs["code"],
        "goal": obs["goal"]
    }
