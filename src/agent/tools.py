from typing import Dict, Any
import os

class Tool:
    def run(self, args: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

class EchoTool(Tool):
    def run(self, args: Dict[str, Any]) -> Dict[str, Any]:
        text = args.get('text','')
        return {'output': text}

class FileReaderTool(Tool):
    def run(self, args: Dict[str, Any]) -> Dict[str, Any]:
        path = args.get('path')
        if not path:
            return {'error': 'no path provided'}
        # Security: only allow reading from a sandboxed directory
        safe_root = os.path.abspath('./sandbox')
        target = os.path.abspath(path)
        if not target.startswith(safe_root):
            return {'error': 'access denied'}
        try:
            with open(target,'r',encoding='utf-8') as f:
                return {'output': f.read()}
        except Exception as e:
            return {'error': str(e)}

class FeishuStubTool(Tool):
    def run(self, args: Dict[str, Any]) -> Dict[str, Any]:
        # Placeholder: replace with real Feishu API calls after registering App
        return {'output': f"feishu_stub called with {args}"}
