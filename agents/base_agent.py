class BaseAgent:
    def __init__(self, name, memory):
        self.name = name
        self.memory = memory

    def run(self, task):
        raise NotImplementedError("Each agent must implement run()")
