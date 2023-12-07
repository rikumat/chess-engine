from services.engine import Engine
from services.ai import Ai
import unittest

ai=Ai()

class TestIntegration(unittest.TestCase):
    def setUp(self):
            pass
    def test_pawn_index_doesnt_overflow(self):
        test_board = [
                [".", ".", ".", ".", ".", ".", ".", "k"],
                ["P", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "p"],
                ["K", ".", ".", ".", ".", ".", ".", "."]
            ]
        engine = Engine(test_board)
        move = ai.calculate_move(engine.board, False)
        self.assertEqual(move, "h2h1")
        engine.make_move(move)
        self.assertEqual(engine.board[6][7], ".")
        self.assertEqual(engine.board[7][7], "q")

    def test_make_move_updates_board_corr(self):
        test_board = [
            ["r", "n", ".", "k", ".", ".", "r", "."],
            ["p", "p", ".", ".", "R", "p", ".", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "p", ".", ".", "p", "B", "."],
            [".", ".", ".", "P", ".", ".", ".", "."],
            ["P", ".", "P", "B", ".", "N", ".", "."],
            [".", ".", "P", ".", ".", ".", ".", "P"],
            [".", ".", "K", ".", ".", ".", ".", "."]
        ]
        engine=Engine(test_board)
        ai.calculate_move(engine.board, False)
        self.assertEqual(engine.board[4][3], "P")