from .node import Node


class Graph:
  def __init__(self):
    self.nodes = []

  def add_node(self, node_id, explored=False):
    if not self.get_node(node_id):
      new_node = Node(node_id, explored)
      self.nodes.append(new_node)

  def __str__(self):
    out = ''
    for node in self.nodes:
      out += str(node)
    return out

  @property
  def explored(self):
    for node in self.nodes:
      if not node.explored:
        return False
    return True

  def get_node(self, id):
    for node in self.nodes:
      if node.id == id:
        return node
    return False

  def add_edge(self, start, end, tetromino):
    self.add_node(start)
    node = self.get_node(start)
    node.add_edge(end, tetromino)

  def pop_node(self, id=''):
    if id == '':
      for node in self.nodes:
        if not node.explored:
          node.explored = True
          return node.id
    else:
      for node in self.nodes:
        if node.id == id:
          node.explored = True
          return id
    return False

  def unexplored_nodes(self):
    out = []
    for node in self.nodes:
      if not node.explored:
        out.append(node.id)
    return out

  def print_node_weights(self):
    print("====== NODE WEIGHTS ======")
    for node in sorted(self.nodes, reverse=True):
      print(node.id, '\t', len(node.edges))

  def prune(self, min_edges=2, recursive=False):
    self.print_node_weights()

    pruned_nodes = []
    for node in self.nodes:
      if len(node.edges) < min_edges:
        pruned_nodes.append(node.id)

    for garb in pruned_nodes:
      node = self.get_node(garb)
      i = self.nodes.index(node)
      del self.nodes[i]

    for garb in pruned_nodes:
      for node in self.nodes:
        node.prune_edge(garb)

    self.print_node_weights()
    if recursive and len(pruned_nodes) > 0:
      self.prune(min_edges, recursive=True)
