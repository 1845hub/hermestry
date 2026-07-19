# Short design notes

- This project is an MVP skeleton for an agent-based system.
- Components:
  - Planner: maps Messages -> Actions. Currently rule-based.
  - Executor: runs Actions by dispatching to Tools.
  - Tools: pluggable adapters (Echo, File Reader, Feishu Stub).
- Security: File read is sandboxed to ./sandbox.
- Future: integrate LLM in Planner, real Feishu API in Tools, persistent state.
