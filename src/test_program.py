from entities.board import Board
from datetime import datetime

board = Board()
test_board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "Q", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", ".", "K", "B", "N", "R"]
        ]

start_time = datetime.now()
for i in range(1000000):
    moves = board.get_diagonal_moves(test_board, "e4")
print((datetime.now()-start_time).total_seconds())