from .models import Message, Action
from typing import List, Optional
import uuid

class Agent:
    def __init__(self, planner, executor):
        self.planner = planner
        self.executor = executor
        self.history: List[Message] = []

    def receive(self, content: str, role: str = 'user') -> dict:
        msg = Message(id=str(uuid.uuid4()), role=role, content=content)
        self.history.append(msg)
        actions = self.planner.plan(msg, self.history)
        results = []
        for act in actions:
            res = self.executor.execute(act)
            results.append(res)
        return {"actions": [a.dict() for a in actions], "results": results}
