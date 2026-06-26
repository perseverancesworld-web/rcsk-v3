from rcsk.core.kernel import CognitiveSwarmKernel

class SwarmNode:
    def __init__(self, node_id: str):
        self.id = node_id
        self.kernel = CognitiveSwarmKernel()

    def process(self, intent: str):
        return self.kernel.step(intent)
