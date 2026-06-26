class Governance:
    def approve(self, evaluation: dict, drift: float = 0.0) -> bool:
        if drift > 0.2 or evaluation.get("score", 0) < 0.6:
            return False
        return True
