from dataclasses import dataclass
from typing import Dict, Protocol
from .world import Graph, shortest_path

@dataclass
class Stats:
    hp: int
    atk: int
    speed: int

class Actor:
    def __init__(self, id: str, room: str, stats: Stats, behavior: "Behavior|None"=None):
        ...

    def is_alive(self) -> bool: ...
    def take_turn(self, graph: Graph, actors: Dict[str,"Actor"], player_id: str) -> dict: ...

class Player(Actor): ...

class Behavior(Protocol):
    def next_action(self, graph: Graph, self_id: str, player_id: str, actors: Dict[str,Actor]) -> dict: ...

class WaitBehavior:
    def next_action(self, graph: Graph, self_id: str, player_id: str, actors: Dict[str,Actor]) -> dict: ...

class ChaseBehavior:
    def __init__(self, sight: int = 999): ...
    def next_action(self, graph: Graph, self_id: str, player_id: str, actors: Dict[str,Actor]) -> dict: ...
