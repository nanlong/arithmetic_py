from arithmetic_py.quick_sort import quick_sort, quick_sort2


def test_quick_sort():
  seq = [2, 1, 4, 3]
  assert quick_sort(seq) == [1, 2, 3, 4]
  
  seq = [2, 1, 4, 3]
  assert quick_sort(seq, lambda x, y: x > y) == [4, 3, 2, 1]

  seq = [4, 7, 8, 2, 3, 9, 6, 0, 4, 4]
  quick_sort2(seq)
  assert seq == [0, 2, 3, 4, 4, 4, 6, 7, 8, 9]
  quick_sort2(seq, order=lambda x, y: x > y)
  assert seq == [9, 8, 7, 6, 4, 4, 4, 3, 2, 0]