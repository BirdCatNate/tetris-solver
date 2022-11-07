from random import randint
from .row import Row


class Board:
  def __init__(self, rows, columns):
    self.rows = rows
    self.columns = columns
    self.board = [Row(columns) for i in range(rows)]

  def __len__(self):
    return len(self.board)

  def __getitem__(self, index):
    return self.board[-index - 1]

  def __setitem__(self, index, value):
    if isinstance(value, Row):
      self.board[index] = value
    else:
      raise Exception('TypeException: Use Row class when setting rows for the board.')

  def __str__(self):
    out = ''
    for row in self.board:
      out += '\t\t\t' + str(row) + '\n'
    return out

  def clear_full_rows(self):
    original = str(self)

    cleared = False
    for row in self.board:
      if row.full:
        cleared = True
        row.clear()
        self.board.remove(row)
        self.board.insert(0, row)
    if cleared:
      print("SUCCESS")
      print(self)
      print(original)

  def try_place_tetronimo(self, x, y, tetronimo):
    failed = False
    floating = True

    for i in reversed(range(len(tetronimo))):
      for j in range(len(tetronimo[i])):
        if tetronimo[i][j] != 0:
          if i + x >= len(self) or j + y >= len(self[i]):
            failed = True
            break
          if i + x - 1 == -1:
            floating = False
          elif self[i + x - 1][j + y] != 0:
            floating = False

          if self[i + x][j + y] != 0:
            failed = True
          self[i + x][j + y] = tetronimo[i][j]

    if failed or floating:
      # print(self)
      # input()
      return False
    self.clear_full_rows()
    return True

  def to_id(self):
    out = ''
    for row in self.board:
      out += ''.join(['0' if int(i) == 0 else '1' for i in row])
    return str(hex(int(out, 2)))[2:]

  def load_from_id(self, id):
    binary = bin(int(id, 16))[1:]

    index = len(binary)
    i = 0
    j = self.columns - 1
    while index > 0 or i < self.rows:
      index -= 1
      if index > 0:
        self[i][j] = binary[index]
      else:
        self[i][j] = 0
      j -= 1
      if j < 0:
        j = self.columns - 1
        i += 1

        if i > self.rows:
          print("FAIL: LOAD FROM ID GOT A NUMBER TOO LARGE")

  @property
  def count(self):
    count = 0
    for row in self.board:
      for entry in row:
        if entry != 0:
          count += 1
    return count
