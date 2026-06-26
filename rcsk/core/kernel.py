from typing import Any
from rcsk.agents.planner import Planner
from rcsk.agents.critic import Critic
from rcsk.agents.executor import Executor
from rcsk.agents.shadow import Shadow
from rcsk.agents.dream import Dream
from rcsk.memory.graph import MemoryGraph
from rcsk.observability.event_log import EventLedger
from rcsk.utils.time import now

class CognitiveSwarmKernel:
    def __init__(self):
        self.memory = MemoryGraph()
        self.ledger = EventLedger()
        self.agents = {
            "planner": Planner(),
            "critic": Critic(),
            "executor": Executor(),
            "shadow": Shadow(),
            "dream": Dream()
        }
        self.ledger.log("init", {"status": "Kernel initialized"})

    def step(self, intent: str, observation: Any = None) -> dict:
        self.ledger.log("step_start", {"intent": intent})

        plan = self.agents["planner"].act(intent, self.memory)
        critique = self.agents["critic"].evaluate(plan, self.memory)
        shadow = self.agents["shadow"].analyze(self.memory)

        decision = self._merge(plan, critique, shadow)

        result = self.agents["executor"].run(decision)

        # Store in memory
        ep_id = self.memory.store(intent, observation, result)

        # Dream compression occasionally
        if len(self.memory.episodes) % 5 == 0:
            dream_result = self.agents["dream"].compress(self.memory)
            self.ledger.log("dream", dream_result)

        self.ledger.log("step_complete", {"episode_id": ep_id, "result": result})
        return result

    def _merge(self, plan: dict, critique: dict, shadow: dict) -> dict:
        return {
            "plan": plan,
            "critique": critique,
            "shadow": shadow,
            "confidence": (critique.get("score", 0.5) + 0.7) / 2
        }

    def get_ledger(self):
        return self.ledger
