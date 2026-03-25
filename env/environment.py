import json
import random
from env.models import Observation, Action, Reward
from env.grader import compute_reward

class EmailEnv:
    def __init__(self):
        with open("data/emails.json") as f:
            self.data = json.load(f)
        self.current = None

    def reset(self):
        self.current = random.choice(self.data)

        return Observation(
            email_text=self.current["email_text"],
            sender_type="customer",
            urgency=self.current["priority"]
        )

    def step(self, action: Action):
        reward_score = compute_reward(action, self.current)

        reward = Reward(
            score=reward_score,
            feedback="Evaluation complete"
        )

        done = True

        return self.reset(), reward, done, {}

    def state(self):
        return self.current