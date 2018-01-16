from arithmetic_py.red_black_tree import RedBlackTree


def test_red_black_tree():
  tree = RedBlackTree()

  tree.put("S", 1)
  tree.put("E", 2)
  tree.put("X", 3)
  tree.put("A", 4)
  tree.put("R", 5)
  tree.put("C", 6)
  tree.put("H", 7)
  tree.put("M", 8)

  assert tree.pre_order() == ['M', 'E', 'C', 'A', 'H', 'S', 'R', 'X']
  assert tree.in_order() == ['A', 'C', 'E', 'H', 'M', 'R', 'S', 'X']
  assert tree.post_order() == ['A', 'C', 'H', 'E', 'R', 'X', 'S', 'M']
  assert tree.level_order() == ['M', 'E', 'S', 'C', 'H', 'R', 'X', 'A']
  
  assert tree.size() == 8

  tree.delete_min()
  assert tree.size() == 7
  assert tree.get("A") is None

  tree.delete_max()
  assert tree.size() == 6
  assert tree.get("X") is None

  tree.delete("S")
  assert tree.size() == 5
  assert tree.get("S") is None