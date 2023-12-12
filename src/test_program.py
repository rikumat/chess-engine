from entities.board import Board
from datetime import datetime

board = Board()
empty_board = [
            [".", ".", ".", ".", ".", ".", ".", "Q"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", "Q", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "Q", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", "Q", ".", "Q", ".", ".", "Q", "."],
            [".", ".", ".", ".", ".", ".", ".", "."]
        ]

start_time = datetime.now()
for i in range(100000):
    moves = board.get_moves_from_board(empty_board, True)
print((datetime.now()-start_time).total_seconds())