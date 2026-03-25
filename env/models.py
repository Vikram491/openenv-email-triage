from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    email_text: str
    sender_type: str
    urgency: str
    history: List[str] = []

class Action(BaseModel):
    classification: str
    priority: str
    response: str

class Reward(BaseModel):
    score: float
    feedback: str