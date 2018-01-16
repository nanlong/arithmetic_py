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


def quick_sort2(seq, start=None, end=None, order=lambda x, y: x < y):
  if start is None:
    start = 0
    
  if end is None:
    end = len(seq) - 1

  if end - start > 0:
    pivot, left, right = seq[start], start, end
    
    while left <= right:
      while order(seq[left], pivot):
        left += 1

      while order(pivot, seq[right]):
        right -= 1

      if left <= right:
        seq[left], seq[right] = seq[right], seq[left]
        left += 1
        right -= 1

    quick_sort2(seq, start, right, order)
    quick_sort2(seq, left, end, order)
