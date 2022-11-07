class Row:
  def __init__(self, length):
    self.length = length
    self.arr = [0 for i in range(length)]

  def __getitem__(self, index):
    return self.arr[index]

  def __setitem__(self, index, value):
    self.arr[index] = int(value)

  def __str__(self):
    out = ''
    for entry in self.arr:
      if entry == 0:
        out += '-  '
      else:
        out += '{}  '.format(entry)
    return out

  def clear(self, value=0):
    for i in range(self.length):
      self.arr[i] = value

  @property
  def full(self):
    for entry in self.arr:
      if entry == 0:
        return False
    return True

  @property
  def empty(self):
    for entry in self.arr:
      if entry != 0:
        return False
      return True

  def __len__(self):
    return self.length


if __name__ == "__main__":
  r = Row(4)
  r[0] = 1
  r[1] = 1
  r[2] = 1
  print(r)
  print('Is the row full? ' + str(r.full))
  print()

  r[3] = 1
  print(r)
  print('Is the row full? ' + str(r.full))
  print()

  arr = [1, 2, 3, 4]
  hydrated = Row.hydrate(arr)
  dehydrated = hydrated.dehydrate()
  print("Starting Arr: " + str(arr))
  print("Hydrated: " + str(hydrated))
  print("Dehydrated: " + str(dehydrated))
