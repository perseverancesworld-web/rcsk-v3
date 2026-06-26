class Critic:
    def evaluate(self, plan: dict, memory) -> dict:
        return {
            "score": 0.75,
            "risks": ["Potential drift in long chains"],
            "suggestions": ["Add more salience weighting"]
        }
