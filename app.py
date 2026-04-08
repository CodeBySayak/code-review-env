import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from fastapi import FastAPI
from env.env import CodeReviewEnv
from env.tasks import EasyTask

import uvicorn

app = FastAPI()

# REQUIRED FOR OPENENV
@app.post("/reset")
def reset():
    env = CodeReviewEnv(EasyTask())
    obs = env.reset()
    return obs

# optional root endpoint
@app.get("/")
def root():
    return {"message": "Code Review Env Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
