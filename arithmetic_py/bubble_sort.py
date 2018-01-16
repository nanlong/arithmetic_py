def bubble_sort(seq, order=lambda x, y: x < y):
  length = len(seq)

  if length <= 1:
    return seq

  while length > 1:
    for i in range(1, length):
      if order(seq[i], seq[i - 1]):
        seq[i], seq[i - 1] = seq[i - 1], seq[i]

    length -= 1

  return seq

    
