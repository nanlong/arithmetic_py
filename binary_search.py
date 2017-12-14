def binary_search(seq, value):
  length = len(seq)
  start = 0
  end = length - 1

  while True:
    if start > end:
      break

    mid = (start + end) / 2
    mid_value = seq[mid]

    if value < mid_value:
      end = mid - 1
    elif value > mid_value:
      start = mid + 1
    elif value == mid_value:
      return mid


if __name__ == '__main__':
    print binary_search([1, 2, 3, 4], 1)
    print binary_search([1, 2, 3, 4], 4)
    print binary_search([1, 2, 3, 4], 5)
    