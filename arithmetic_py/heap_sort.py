def heap_sort(seq, order=lambda x, y: x < y):
  length = len(seq)

  for start in xrange(length / 2 - 1, -1, -1):
    sift_down(seq, start, length - 1, order)

  for finish in xrange(length - 1, 0, - 1):
    seq[0], seq[finish] = seq[finish], seq[0]
    sift_down(seq, 0, finish - 1, order)

  return seq

def sift_down(seq, start, finish, order):
  root = start

  while True:
    child = root * 2 + 1

    if child > finish:
      break

    if child + 1 <= finish and order(seq[child], seq[child + 1]):
      child += 1

    if order(seq[root], seq[child]):
      seq[root], seq[child] = seq[child], seq[root]
      root = child
    else:
      break

if __name__ == '__main__':
  seq = [2, 1, 4, 3]
  assert heap_sort(seq) == [1, 2, 3, 4]

  seq = [2, 1, 4, 3]
  assert heap_sort(seq, lambda x, y: x > y) == [4, 3, 2, 1]
    