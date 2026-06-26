import networkx as nx
from dataclasses import dataclass
from typing import Dict, Any, List
from rcsk.utils.ids import generate_id
from rcsk.utils.time import now

@dataclass
class Episode:
    id: str
    intent: str
    observation: Any
    result: Any
    timestamp: float
    salience: float = 1.0
    parents: List[str] = None

    def __post_init__(self):
        if self.parents is None:
            self.parents = []

class MemoryGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.episodes: Dict[str, Episode] = {}

    def store(self, intent: str, observation: Any, result: Any, parent_ids: List[str] = None) -> str:
        ep_id = generate_id("ep_")
        episode = Episode(
            id=ep_id,
            intent=intent,
            observation=observation,
            result=result,
            timestamp=now(),
            parents=parent_ids or []
        )
        self.episodes[ep_id] = episode
        self.graph.add_node(ep_id, data=episode)
        for parent in episode.parents:
            self.graph.add_edge(parent, ep_id)
        return ep_id

    def get_causal_chain(self, episode_id: str) -> List[Episode]:
        if episode_id not in self.graph:
            return []
        chain = []
        current = episode_id
        while current:
            chain.append(self.episodes[current])
            predecessors = list(self.graph.predecessors(current))
            current = predecessors[0] if predecessors else None
        return list(reversed(chain))

    def get_top_salient(self, n: int = 10) -> List[Episode]:
        return sorted(self.episodes.values(), key=lambda e: e.salience, reverse=True)[:n]
