import pytest
from agent.planner import Planner
from agent.models import Message

def test_planner_echo():
    p = Planner()
    m = Message(id='1', role='user', content='echo hello')
    acts = p.plan(m, [])
    assert len(acts) == 1
    assert acts[0].name == 'echo'
