def is_red(node):
  if node:
    return node.color == "red"
  else:
    return False


def size(node):
  if node:
    return node.n
  else:
    return 0


class Node:

  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.n = 1
    self.color = "red"
    self.left = None
    self.right = None

  def get(self, key):
    if key < self.key and self.left:
      return self.left.get(key)
    elif key > self.key and self.right:
      return self.right.get(key)
    elif key == self.key:
      return self

  def put(self, key, val):
    if key < self.key:
      if self.left:
        self.left = self.left.put(key, val)
      else:
        self.left = Node(key, val)
    elif key > self.key:
      if self.right:
        self.right = self.right.put(key, val)
      else:
        self.right = Node(key, val)
    else:
      self.val = val

    self = self.balance()
    return self

  def update_size(self):
    self.n = size(self.left) + size(self.right) + 1

  def rotate_left(self):
    h = self
    x = self.right

    x.color = h.color
    x.n = h.n

    h.color = "red"
    h.right = x.left
    h.update_size()

    x.left = h

    return x

  def rotate_right(self):
    h = self
    x = self.left

    x.color = h.color
    x.n = h.n

    h.color = "red"
    h.left = x.right
    h.update_size()

    x.right = h
    
    return x


  def flip_colors(self):
    self.color = "red" if self.color == "black" else "black"

    if self.left:
      self.left.color = "red" if self.left.color == "black" else "black"

    if self.right:
      self.right.color = "red" if self.right.color == "black" else "black"

  def balance(self):
    if not is_red(self.left) and is_red(self.right):
      self = self.rotate_left()

    if is_red(self.left) and (self.left and is_red(self.left.left)):
      self = self.rotate_right()

    if is_red(self.left) and is_red(self.right):
      self.flip_colors()

    self.update_size()
    return self

  def move_red_left(self):
    self.flip_colors()

    if self.right and is_red(self.right.left):
      self.right = self.right.rotate_left()
      self = self.rotate_right()

    return self

  def move_red_right(self):
    self.flip_colors()

    if self.left and is_red(self.left.left):
      self = self.rotate_right()

    return self

  def min(self):
    if self.left:
      return self.left.min()
    
    return self

  def delete_min(self):
    if not (self.left and is_red(self.left.left)):
      self = self.move_red_left()

    if self.left is None:
      return None

    self.left = self.left.delete_min()
    return self.balance()

  def delete_max(self):
    if is_red(self.left):
      self = self.rotate_right()

    if self.right is None:
      return None
      
    if not (self.right and is_red(self.right.left)):
      self = self.move_red_right()

    self.right = self.right.delete_max()
    return self.balance()

  def delete(self, key):
    if key < self.key:
      if not (self.left and is_red(self.left.left)):
        self = self.move_red_left()

      self = self.left.delete(key)
    else:
      if is_red(self.left):
        self = self.rotate_right()

      if key == self.key and not self.right:
        return None

      if not (self.right and is_red(self.right.left)):
        self = self.move_red_right()

      if key == self.key:
        x = self.right.min()

        self.key = x.key
        self.val = x.val
        self.n = x.n

        self.right = self.right.delete_min()
      else:
        self.right = self.right.delete(key)

    return self.balance()

  def pre_order(self):
    stack = [self]
    res = []
    
    while len(stack):
      node = stack.pop()
      res.append(node.key)

      if node.right:
        stack.append(node.right)

      if node.left:
        stack.append(node.left)

    return res

  def in_order(self):
    stack = []
    res = []
    p = self

    while p or len(stack):
      while p:
        stack.append(p)
        p = p.left

      cur = stack.pop()
      res.append(cur.key)
      p = cur.right

    return res

  def post_order(self):
    stack = [self]
    res = []
    
    while len(stack):
      node = stack.pop()
      res.append(node.key)

      if node.left:
        stack.append(node.left)

      if node.right:
        stack.append(node.right)

    res.reverse()
    return res

  def level_order(self):
    from collections import deque
    queue = deque([self])
    res = []

    while len(queue):
      node = queue.popleft()
      res.append(node.key)

      if node.left:
        queue.append(node.left)

      if node.right:
        queue.append(node.right)

    return res

    
class RedBlackBST:

  def __init__(self):
    self.root = None

  def get(self, key):
    if self.root:
      return self.root.get(key)

  def put(self, key, val):
    if self.root:
      self.root = self.root.put(key, val)
    else:
      self.root = Node(key, val)

    self.root.color = "black"

  def delete(self, key):
    if self.root:
      if not is_red(self.root.left) and not is_red(self.root.right):
        self.root.color = "red"

      self.root = self.root.delete(key)

      if self.size() > 0:
        self.root.color = "black"

  def delete_min(self):
    if self.root:
      if not is_red(self.root.left) and not is_red(self.root.right):
        self.root.color = "red"

      self.root = self.root.delete_min()

      if self.size() > 0:
        self.root.color = "black"

  def delete_max(self):
    if self.root:
      if not is_red(self.root.left) and not is_red(self.root.right):
        self.root.color = "red"

      self.root = self.root.delete_max()

      if self.size() > 0:
        self.root.color = "black"

  def size(self):
    return size(self.root)

  def pre_order(self):
    if self.root:
      return self.root.pre_order()
    return []

  def in_order(self):
    if self.root:
      return self.root.in_order()
    return []

  def post_order(self):
    if self.root:
      return self.root.post_order()
    return []

  def level_order(self):
    if self.root:
      return self.root.level_order()
    return []

if __name__ == '__main__':
    tree = RedBlackBST()

    tree.put("S", 1)
    tree.put("E", 2)
    tree.put("X", 3)
    tree.put("A", 4)
    tree.put("R", 5)
    tree.put("C", 6)
    tree.put("H", 7)
    tree.put("M", 8)

    assert tree.pre_order() == ['M', 'E', 'C', 'A', 'H', 'S', 'R', 'X']
    assert tree.in_order() == ['A', 'C', 'E', 'H', 'M', 'R', 'S', 'X']
    assert tree.post_order() == ['A', 'C', 'H', 'E', 'R', 'X', 'S', 'M']
    assert tree.level_order() == ['M', 'E', 'S', 'C', 'H', 'R', 'X', 'A']
   
    assert tree.size() == 8

    tree.delete_min()
    assert tree.size() == 7
    assert tree.get("A") is None

    tree.delete_max()
    assert tree.size() == 6
    assert tree.get("X") is None

    tree.delete("S")
    assert tree.size() == 5
    assert tree.get("S") is None

    