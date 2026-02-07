from pydantic import BaseModel
from typing import List

class TopicInput(BaseModel):
    name: str
    difficulty: int
    confidence: int
    deadline_days: int
    weight: float = 1.0


class PlanRequest(BaseModel):
    daily_hours: float
    learning_pace: str
    topics: List[TopicInput]
