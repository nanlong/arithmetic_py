def binary_search(seq, value):
  length = len(seq)
  start = 0
  end = length - 1

  while True:
    if start > end:
      break

    mid = (start + end) // 2
    mid_value = seq[mid]

    if value < mid_value:
      end = mid - 1
    elif value > mid_value:
      start = mid + 1
    elif value == mid_value:
      return mid


if __name__ == '__main__':
  seq = [1, 2, 3, 4]
  assert binary_search(seq, 1) == 0
  assert binary_search(seq, 4) == 3
  assert binary_search(seq, 5) is None
    