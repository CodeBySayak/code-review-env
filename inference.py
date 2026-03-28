import os
from openai import OpenAI

from env.env import CodeReviewEnv
from env.tasks import EasyTask, MediumTask, HardTask

API_BASE_URL = "https://router.huggingface.co/v1"
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"
import os
HF_TOKEN = os.getenv("HF_TOKEN")
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def get_action(prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=20,
        )
        return response.choices[0].message.content.strip()
    except:
        return "flag_security" 

def run(task):
    env = CodeReviewEnv(task)
    obs = env.reset()

    prompt = f"""
You are a security code reviewer.

Code:
{obs['code']}

Choose one:
approve / request_changes / reject / flag_security
"""

    action = get_action(prompt)

    _, reward, _, _ = env.step(action)
    return reward


if __name__ == "__main__":
    tasks = [EasyTask(), MediumTask(), HardTask()]
    scores = []

    for t in tasks:
        r = run(t)
        print("Score:", r)
        scores.append(r)

    print("Average:", sum(scores)/len(scores))