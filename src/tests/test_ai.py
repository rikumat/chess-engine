import unittest
from services.ai import Ai
from services.move_generator import MoveGenerator

empty_board = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."]
        ]
class TestAi(unittest.TestCase):
    def setUp(self):
        self.ai=Ai(MoveGenerator())
        pass
    def test_ai_notices_easy_checkmate(self):
        test_board = [
            ["k", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", "P", "P", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["K", ".", ".", ".", "Q", ".", ".", "."]
        ]
        value, move =self.ai.calculate_move(test_board, True)
        self.assertEqual(move, "e1e8")

    def test_ai_notices_medium_checkmate(self):
        #r1bq2r1/b4pk1/p1pp1p2/1p2pP2/1P2P1PB/3P4/1PPQ2P1/R3K2R w

        test_board = [
            ["r", ".", "b", "q", ".", ".", "r", "."],
            ["b", ".", ".", ".", ".", "p", "k", "."],
            ["p", ".", "p", "p", ".", "p", ".", "."],
            [".", "p", ".", ".", "p", "P", ".", "."],
            [".", "P", ".", ".", "P", ".", "P", "B"],
            [".", ".", ".", "P", ".", ".", ".", "."],
            [".", "P", "P", "Q", ".", ".", "P", "."],
            ["R", ".", ".", ".", ".", "K", ".", "R"]
        ]
        value, move =self.ai.calculate_move(test_board, True)
        self.assertEqual(move, "d2h6")

    def test_ai_notices_blunder(self):
        test_board = [
            ["r", ".", "b", ".", "k", "b", "n", "r"],
            ["p", "p", "B", "n", ".", "p", "p", "p"],
            [".", ".", ".", ".", "p", "q", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "P", "Q", ".", ".", "."],
            [".", ".", "P", ".", ".", ".", ".", "."],
            ["P", "P", ".", ".", "B", "P", "P", "P"],
            ["R", "N", ".", ".", "K", ".", "N", "R"]
        ]
        value, move =self.ai.calculate_move(test_board, False)
        self.assertEqual(move, "f6g5")

    def test_ai_prevents_promotion(self):
        test_board = [
            ["k", ".", ".", ".", ".", ".", ".", "."],
            [".", "R", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "B", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "r", "."],
            ["p", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "K"]
        ]
        value, move =self.ai.calculate_move(test_board, False)
        self.assertEqual(move, "a2a1")

    def test_ai_prevents_promotion2(self):
        test_board = [
            ["k", ".", ".", ".", ".", ".", "r", "."],
            [".", ".", ".", ".", "R", ".", ".", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "N", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "K"]
        ]

        value, move =self.ai.calculate_move(test_board, False)
        self.assertEqual(move[3], "8")
        self.assertNotEqual(move[2], "e")


