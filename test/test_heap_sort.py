from arithmetic_py.heap_sort import heap_sort


def test_heap_sort():
  seq = [2, 1, 4, 3]
  assert heap_sort(seq) == [1, 2, 3, 4]

  seq = [2, 1, 4, 3]
  assert heap_sort(seq, lambda x, y: x > y) == [4, 3, 2, 1]