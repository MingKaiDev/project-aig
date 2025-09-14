from game.world import build_world
from game.actors import Actor, Player, Stats, ChaseBehavior, WaitBehavior

def setup_pair():
    g = build_world(8, seed=5)
    rooms = list(g.keys())
    p = Player("P", rooms[0], Stats(hp=10, atk=3, speed=1))
    e = Actor("E", rooms[-1], Stats(hp=5, atk=2, speed=1), behavior=ChaseBehavior())
    actors = {"P": p, "E": e}
    return g, actors

def test_wait_behavior_does_nothing():
    g, actors = setup_pair()
    a = actors["E"]
    a.set_behavior(WaitBehavior())
    action = a.take_turn(g, actors, "P")
    assert action["type"] in {"wait","noop"}

def test_chase_behavior_moves_toward_player():
    g, actors = setup_pair()
    e = actors["E"]
    p = actors["P"]
    e_room_before = e.room
    act = e.take_turn(g, actors, "P")
    assert act["type"] in {"move","attack"}
    if act["type"] == "move":
        assert act["to"] in g[e_room_before]
