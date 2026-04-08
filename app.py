import sys
import os

# Fix import path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from fastapi import FastAPI
from env.env import CodeReviewEnv
from env.tasks import EasyTask

app = FastAPI()

# REQUIRED endpoint for OpenEnv
@app.post("/reset")
def reset():
    env = CodeReviewEnv(EasyTask())
    obs = env.reset()
    return obs

# Optional root endpoint
@app.get("/")
def root():
    return {"message": "Code Review Env Running"}
