import unittest
from services.ai import Ai

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
        self.ai = Ai()

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
        move = self.ai.calculate_move(test_board, True)
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
        move = self.ai.calculate_move(test_board, True)
        self.assertEqual(move, "d2h6")

    def test_ai_can_solve_puzzle_1(self):
        #2r3k1/p4p2/3Rp2p/1p2P1pK/8/1P4P1/P3Q2P/1q6 b - - 0 1
        test_board = [
            [".", ".", "r", ".", ".", ".", "k", "."],
            ["p", ".", ".", ".", ".", "p", ".", "."],
            [".", ".", ".", "R", "p", ".", ".", "p"],
            [".", "p", ".", ".", "P", ".", "p", "K"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", "P", ".", ".", ".", ".", "P", "."],
            ["P", ".", ".", ".", "Q", ".", ".", "P"],
            [".", "q", ".", ".", ".", ".", ".", "."]
        ]
        move1 = self.ai.calculate_move(test_board, False)
        self.assertEqual(move1, "b1g6")


    def test_ai_values_locations_correctly(self):
        test_board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "P", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", ".", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        move = self.ai.calculate_move(test_board, False)
        self.assertEqual(move, "e7e5")

    def test_ai_notices_promotion(self):
        test_board = [
            ["k", ".", ".", ".", ".", ".", ".", "."],
            [".", "R", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "B", ".", ".", ".", ".", "."],
            ["p", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "r", "."],
            ["P", ".", ".", ".", ".", ".", ".", "K"]
        ]
        move = self.ai.calculate_move(test_board, False)
        self.assertEqual(move, "2")



