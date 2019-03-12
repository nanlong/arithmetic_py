from random import randint

class LinkedNode:

  def __init__(self, data=None, prev_node=None, next_node=None):
    self.data = data
    self.prev_node = prev_node
    self.next_node = next_node


class LinkedList:

  def __init__(self):
    self.head = LinkedNode()
    self.tail = LinkedNode()
    self.head.next_node = self.tail
    self.tail.prev_node = self.head

  def build(self, n):
    prev_node = self.head

    for _ in range(n):
      data = randint(0, 100)
      node = LinkedNode(data, prev_node=prev_node, next_node=self.tail)
      prev_node.next_node = node
      self.tail.prev_node = node
      prev_node = node

    return self.head, self.tail


class Solution:

  def quick_sort(self, head, low, high):
    if not head and not head.next_node or low == high:
      return

    h, t = low, high
    k = h.data

    while h != t:

      while h != t and t.data >= k:
        t = t.prev_node

      h.data = t.data

      while h != t and h.data <= k:
        h = h.next_node

      t.data = h.data

    h.data = k

    if low != h:
      self.quick_sort(head, low, h.prev_node)

    if h != high:
      self.quick_sort(head, h.next_node, high)


if __name__ == "__main__":
  h, t = LinkedList().build(10)

  curr = h
  data = []
  while curr.next_node:
    data.append(curr.next_node.data)
    curr = curr.next_node
  print(data)

  Solution().quick_sort(h.next_node, h.next_node, t.prev_node)

  curr = h
  data = []
  while curr.next_node:
    data.append(curr.next_node.data)
    curr = curr.next_node
  print(data)
