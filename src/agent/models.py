from pydantic import BaseModel
from typing import Any, Dict

class Message(BaseModel):
    id: str
    role: str  # 'user'|'system'|'agent'
    content: str
    metadata: Dict[str, Any] = {}

class Action(BaseModel):
    name: str
    args: Dict[str, Any] = {}
