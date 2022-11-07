from core.board import Board
from time import sleep
from core.tetronimo import get_rotations

# The problem is as follows:
#
# You are given a 4x4 tetris board of the following initial state:
# 0 0 0 0
# 0 0 0 0
# 1 1 0 0
# 1 0 0 0
# Upon placing a tetris piece, if an entire row is full it gets cleared.
#
# Your objective is to get the longest possible combo under the following conditions
# 0. You only get to see the current piece, and can illegally place tetronimos.
# 1. You only get to see the current piece
# 2. You only get to see the next X pieces
# 3. You see the next X pieces, and can hold a piece if necessary.
from core.graph import Graph

graph = Graph()
board = Board(4, 4)


def build_entire_graph(starting_state, tetrominos, exclude_states, automate=0):
  for state in exclude_states:
    graph.add_node(state, True)
  graph.add_node(starting_state)

  while not graph.explored:
    start = ''

    if automate > 8:
      start = graph.pop_node()
    else:
      while start == '':
        print('Valid points to explore:', graph.unexplored_nodes())
        next_node = input('Explore which node next? ')
        if graph.pop_node(next_node):
          start = next_node

    board.load_from_id(start)
    print("Exploring STATE:", start)
    print(board)
    print(board)
    if automate < 9:
      input("Press enter to continue...")
    for tetronimo in tetrominos:
      print("Finding solutions for " + tetronimo + "...")
      for i in range(4):
        for j in range(4):
          for rotation in get_rotations(tetronimo):
            board.load_from_id(start)
            if board.try_place_tetronimo(i, j, rotation):
              if board.count == 3:
                end = board.to_id()
                graph.add_edge(start, end, tetronimo)
                graph.add_node(end)
                print(start, "->", end, 'using', tetronimo)
                if automate < 3:
                  input()
    print()
    print("============ GRAPH AFTER EXPLORING", start, " ============")
    print(graph)
    if automate < 10:
      input("Press enter to continue...")


first_state = (
  (0, 0, 0, 0),
  (0, 0, 0, 0),
  (9, 9, 0, 0),
  (9, 0, 0, 0)
)

all_pieces = sorted(['i', 'j', 'l', 'o', 's', 't', 'z'])
# build_entire_graph('c8', all)
build_entire_graph(
  'c8',
  all_pieces,
  [],
  10
)
print()
print("============ PRUNING TIME ============")
graph.prune(min_edges=4, recursive=True)
print()
print("============ FINAL GRAPH ============")
print(graph)
for node in sorted(graph.nodes):
  board.load_from_id(node.id)
  print(board)
  print("BOARD:", node.id)
  input()
