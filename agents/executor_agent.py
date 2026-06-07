from agents.base_agent import BaseAgent

class ExecutorAgent(BaseAgent):
    def run(self, task):
        execution = f"[Execution] Completed task: {task}"
        self.memory.store("execution", execution)
        return execution
