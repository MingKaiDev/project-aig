from game.world import build_world, is_connected, neighbors

def test_world_connected():
    g = build_world(10, seed=42)
    start = next(iter(g.keys()))
    assert is_connected(g, start)

def test_neighbors_nonempty():
    g = build_world(8, seed=1)
    for r in g:
        assert len(neighbors(g, r)) >= 1
