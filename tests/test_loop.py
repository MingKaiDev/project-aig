from game.game import init_game, legal_moves, apply_action

def test_init_and_first_move():
    g, actors, pid, eid = init_game(seed=9)
    room = actors[pid].room
    moves = legal_moves(g, room)
    assert len(moves) > 0
    action = {"type":"move","actor":pid,"to":moves[0]}
    apply_action(action, g, actors)
    assert actors[pid].room == moves[0]
