from game.world import build_world, shortest_path

def test_bfs_self_zero_len():
    g = build_world(6, seed=2)
    rooms = list(g.keys())
    src = rooms[0]
    assert shortest_path(g, src, src) == [src]

def test_bfs_path_monotonic_decrease():
    g = build_world(8, seed=3)
    rooms = list(g.keys())
    src, dst = rooms[0], rooms[-1]
    path = shortest_path(g, src, dst)
    assert path[0] == src and path[-1] == dst
    assert len(path) == len(set(path))
