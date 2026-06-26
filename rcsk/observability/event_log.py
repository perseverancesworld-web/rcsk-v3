from dataclasses import dataclass
from typing import List, Dict, Any
from rcsk.utils.time import now
from rcsk.utils.ids import generate_id

@dataclass
class Event:
    id: str
    timestamp: float
    event_type: str
    data: Dict[str, Any]

class EventLedger:
    def __init__(self):
        self.events: List[Event] = []

    def log(self, event_type: str, data: Dict[str, Any]):
        event = Event(
            id=generate_id("evt_"),
            timestamp=now(),
            event_type=event_type,
            data=data
        )
        self.events.append(event)
        return event.id

    def get_recent(self, n: int = 50) -> List[Event]:
        return self.events[-n:]

    def replay(self) -> List[Event]:
        return self.events[:]
