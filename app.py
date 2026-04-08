import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import gradio as gr
from env.env import CodeReviewEnv
from env.tasks import EasyTask

def run_env():
    env = CodeReviewEnv(EasyTask())
    obs = env.reset()
    return str(obs)

iface = gr.Interface(
    fn=run_env,
    inputs=[],
    outputs="text",
    title="AI Code Review Environment"
)

iface.launch(server_name="0.0.0.0", server_port=7860)
