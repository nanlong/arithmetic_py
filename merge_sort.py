def merge_sort(seq, order=lambda x, y: x < y):
  length = len(seq)

  if length <= 1:
    return seq

  pivot = length / 2
  left = merge_sort(seq[:pivot], order)
  right = merge_sort(seq[pivot:], order)

  return merge(left, right, order)

def merge(x, y, order):
  result = []
  i, j = 0, 0
  x_len, y_len = len(x), len(y)

  while i < x_len and j < y_len:
    if order(x[i], y[j]):
      result.append(x[i])
      i += 1
    else:
      result.append(y[j])
      j += 1

  if i < x_len:
    result.extend(x[i:])

  if j < y_len:
    result.extend(y[j:])

  return result


if __name__ == '__main__':
  seq = [2, 1, 4, 3]
  assert merge_sort(seq) == [1, 2, 3, 4]

  seq = [2, 1, 4, 3]
  assert merge_sort(seq, lambda x, y: x > y) == [4, 3, 2, 1]
    