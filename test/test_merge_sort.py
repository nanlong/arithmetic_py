from arithmetic_py.merge_sort import merge_sort


def test_merge_sort():
  seq = [2, 1, 4, 3]
  assert merge_sort(seq) == [1, 2, 3, 4]

  seq = [2, 1, 4, 3]
  assert merge_sort(seq, lambda x, y: x > y) == [4, 3, 2, 1]