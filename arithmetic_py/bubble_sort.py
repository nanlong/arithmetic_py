def bubble_sort(seq, order=lambda x, y: x < y):
  length = len(seq)

  if length <= 1:
    return seq

  while length > 1:
    for i in xrange(1, length):
      if order(seq[i], seq[i - 1]):
        seq[i], seq[i - 1] = seq[i - 1], seq[i]

    length -= 1

  return seq


if __name__ == '__main__':
    seq = [2, 1, 4, 3]
    assert bubble_sort(seq) == [1, 2, 3, 4]
    
    seq = [2, 1, 4, 3]
    assert bubble_sort(seq, lambda x, y: x > y) == [4, 3, 2, 1]
    
