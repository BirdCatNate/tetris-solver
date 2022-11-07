from core.board import Board

board = Board(4, 4)
board.load_from_id('c8')
print(board.to_id())
