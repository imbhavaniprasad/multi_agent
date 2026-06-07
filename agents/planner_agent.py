from agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def run(self, task):
        plan = f"[Plan] Steps to solve: {task}"
        self.memory.store("plan", plan)
        return plan
