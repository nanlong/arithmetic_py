def quick_sort(seq, order=lambda x, y: x < y):
  if len(seq) <= 1:
    return seq

  pivot = seq[0]
  left, right = [], []

  for item in seq[1:]:
    if order(item, pivot):
      left.append(item)
    else:
      right.append(item)

  return quick_sort(left, order) + [pivot] + quick_sort(right, order)


if __name__ == '__main__':
    seq = [2, 1, 4, 3]
    print quick_sort(seq)
    