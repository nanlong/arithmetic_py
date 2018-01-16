# utf8
from collections import defaultdict

class Graph:

  def __init__(self):
    self._v = 0
    self._e = 0
    self._adj = defaultdict(list)

  def add_edge(self, v, e):
    if v not in self._adj.keys():
      self._v += 1

    if e not in self._adj.keys():
      self._v += 1

    self._adj[v].append(e)
    self._adj[e].append(v)
    self._e += 1

  def v(self):
    return self._v

  def e(self):
    return self._e

  def adj(self, v):
    return reversed(self._adj[v])

  # 计算v的度数
  def degree(self, v):
    return len(self.adj(v))

  # 计算所有顶点的最大度数
  def max_degree(self):
    res = (None, 0)
    for v in self._adj.keys():
      if self.degree(v) > res[1]:
        res = (v, self.degree(v))
    return res

  # 计算所有顶点的平均度数
  def avg_degree(self):
    return 2 * self.e() / self.v()

  def __str__(self):
    s = "{} vertices, {} edges \n".format(self.v(), self.e())

    for v in self._adj.keys():
      s += "{}: ".format(v)
      for w in self.adj(v):
        s += "{} ".format(w)
      s += "\n"

    return s
        

class DepthFirstSearch:
  
  def __init__(self, g, s):
    self._marked = defaultdict(bool)
    self._count = 0
    self.dfs(g, s)

  def dfs(self, g, v):
    self._marked[v] = True
    self._count += 1

    for w in g.adj(v):
      if not self.marked(w):
        self.dfs(g, w)

  def marked(self, v):
    return self._marked[v]

  def count(self):
    return self._count


class DepthFirstPaths:
  
  def __init__(self, g, s):
    self._marked = defaultdict(bool)
    self._edge_to = {}
    self._s = s
    self.dfs(g, s)

  def dfs(self, g, v):
    self._marked[v] = True

    for w in g.adj(v):
      if not self.marked(w):
        self._edge_to[w] = v
        self.dfs(g, w)

  def marked(self, v):
    return self._marked[v]

  def has_path_to(self, v):
    return self.marked(v)

  def path_to(self, v):
    if not self.has_path_to(v):
      return None

    path = []
    x = v

    while x != self._s:
      path.append(x)
      x = self._edge_to[x]

    path.append(self._s)
    return path


class BreadthFirstPaths:
  
  def __init__(self, g, s):
    self._marked = defaultdict(bool)
    self._edge_to = {}
    self._s = s
    self.bfs(g, s)

  def marked(self, v):
    return self._marked[v]

  def bfs(self, g, v):
    from collections import deque
    queue = deque()
    self._marked[v] = True
    queue.append(v)

    while len(queue):
      v = queue.popleft()

      for w in g.adj(v):
        if not self.marked(w):
          self._marked[w] = True
          self._edge_to[w] = v
          queue.append(w)

  def has_path_to(self, v):
    return self.marked(v)

  def path_to(self, v):
    if not self.has_path_to(v):
      return None

    path = []
    x = v

    while x != self._s:
      path.append(x)
      x = self._edge_to[x]

    path.append(self._s)
    return list(reversed(path))

    
    