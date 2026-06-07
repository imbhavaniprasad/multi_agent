from agents.researcher_agent import ResearcherAgent
from agents.planner_agent import PlannerAgent
from agents.executor_agent import ExecutorAgent
from memory.shared_memory import SharedMemory

class Orchestrator:
    def __init__(self):
        self.memory = SharedMemory()
        self.researcher = ResearcherAgent("Researcher", self.memory)
        self.planner = PlannerAgent("Planner", self.memory)
        self.executor = ExecutorAgent("Executor", self.memory)

    def run(self, task):
        research = self.researcher.run(task)
        plan = self.planner.run(task)
        execution = self.executor.run(task)

        return {
            "research": research,
            "plan": plan,
            "execution": execution,
            "memory": self.memory.get_all()
        }
