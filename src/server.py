from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent.planner import Planner
from agent.executor import Executor
from agent.core import Agent

app = FastAPI(title='hermestry')
planner = Planner()
executor = Executor()
agent = Agent(planner, executor)

class Input(BaseModel):
    text: str

@app.post('/message')
async def message(inp: Input):
    return agent.receive(inp.text)

@app.get('/health')
async def health():
    return {'status':'ok'}
