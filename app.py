from fastapi import FastAPI
from env.environment import EmailEnv
from env.models import Action
from env.tasks import get_tasks
from env.grader import grader

app = FastAPI()
env = EmailEnv()

@app.get("/")
def home():
    return {"message": "OpenEnv Email Triage Running"}

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done
    }

@app.get("/tasks")
def tasks():
    return get_tasks()

@app.get("/state")
def state():
    return env.state()

@app.post("/grader")
def grade(action: Action, task: str = "hard"):
    gt = env.state()
    score = grader(action, gt, task)
    return {"score": score}

@app.get("/baseline")
def baseline():
    results = {}

    for task in ["easy", "medium", "hard"]:
        env.reset()

        action = Action(
            classification="query",
            priority="medium",
            response="Thanks for your email"
        )

        score = grader(action, env.state(), task)
        results[task] = score

    return results