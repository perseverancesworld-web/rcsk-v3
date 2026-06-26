class Executor:
    def run(self, decision: dict) -> dict:
        # Simulate execution
        return {
            "status": "success",
            "output": f"Executed: {decision.get('plan', {})}",
            "metrics": {"latency": 0.45}
        }
