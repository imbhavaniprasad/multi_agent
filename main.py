from orchestrator.orchestrator import Orchestrator

if __name__ == "__main__":
    orchestrator = Orchestrator()

    task = "Build a trading bot using EMA strategy"
    result = orchestrator.run(task)

    print("\nFinal Output:")
    for k, v in result.items():
        print(f"{k}: {v}")
