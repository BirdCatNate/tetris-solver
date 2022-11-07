class Node:
  def __init__(self, id, explored):
    self.id = id
    self.explored = explored
    self.edges = {}

  def add_edge(self, end, tetromino):
    if end not in self.edges:
      self.edges[end] = set()
    self.edges[end].add(tetromino)

  def __str__(self):
    out = ''
    for edge in sorted(self.edges):
      pieces = self.edges[edge]
      out += self.id + ' ' + edge + ' ' + ''.join(sorted(pieces)) + '\n'
    return out

  def __lt__(self, other):
    return len(self.edges) < len(other.edges)

  def prune_edge(self, end):
    if end in self.edges:
      del self.edges[end]
