class Planner:
    def act(self, intent: str, memory) -> dict:
        # Simple forward planning
        return {
            "steps": [f"Step 1: Analyze {intent}", "Step 2: Execute plan"],
            "expected_outcome": f"Successful handling of {intent}"
        }
