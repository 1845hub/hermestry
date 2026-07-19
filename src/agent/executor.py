from .models import Action
from typing import Any, Dict
from .tools import EchoTool, FileReaderTool, FeishuStubTool

class Executor:
    def __init__(self):
        self.tools = {
            'echo': EchoTool(),
            'read_file': FileReaderTool(),
            'feishu': FeishuStubTool(),
        }

    def execute(self, action: Action) -> Dict[str, Any]:
        tool = self.tools.get(action.name)
        if not tool:
            return {'error': f'unknown action {action.name}'}
        return tool.run(action.args)
