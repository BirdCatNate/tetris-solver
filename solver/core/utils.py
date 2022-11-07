def printable_arr(arr):
  out = ''
  for row in reversed(arr):
    out += '\t\t\t'
    for entry in row:
      out += str(entry) + '  '
    out += '\n'
  return out
