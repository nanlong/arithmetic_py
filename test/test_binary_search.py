from arithmetic_py.binary_search import binary_search


def test_binary_search():
  seq = [1, 2, 3, 4]
  assert binary_search(seq, 1) == 0
  assert binary_search(seq, 4) == 3
  assert binary_search(seq, 5) is None