from typing import List
from .models import Message, Action

class Planner:
    """A simple rule/template-driven planner. Replace with LLM-based planner later."""
    def plan(self, message: Message, history: List[Message]) -> List[Action]:
        text = message.content.strip().lower()
        if text.startswith('echo '):
            payload = message.content[len('echo '):]
            return [Action(name='echo', args={'text': payload})]
        if text.startswith('readfile '):
            path = message.content[len('readfile '):].strip()
            return [Action(name='read_file', args={'path': path})]
        # default: reply
        return [Action(name='respond', args={'text': message.content})]
