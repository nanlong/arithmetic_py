from arithmetic_py.graph import Graph, DepthFirstSearch, BreadthFirstPaths


def test_graph():
  tiny_g = [
    (0, 5),
    (2, 4),
    (2, 3),
    (1, 2),
    (0, 1),
    (3, 4),
    (3, 5),
    (0, 2),
  ]

  g = Graph()

  for v, e in tiny_g:
    g.add_edge(v, e)

  dfs = DepthFirstSearch(g, 0)
  assert dfs.marked(3) == True
  assert dfs.count() == 6

  d_path = BreadthFirstPaths(g, 0)
  assert d_path.path_to(3) == [0, 2, 3]

  b_path = BreadthFirstPaths(g, 0)
  assert b_path.path_to(3) == [0, 2, 3]