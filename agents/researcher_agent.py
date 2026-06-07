from agents.base_agent import BaseAgent

class ResearcherAgent(BaseAgent):
    def run(self, task):
        result = f"[Research] Found information about: {task}"
        self.memory.store("research", result)
        return result
