from arithmetic_py.bubble_sort import bubble_sort


def test_bubble_sort():
  seq = [2, 1, 4, 3]
  assert bubble_sort(seq) == [1, 2, 3, 4]
  
  seq = [2, 1, 4, 3]
  assert bubble_sort(seq, lambda x, y: x > y) == [4, 3, 2, 1]