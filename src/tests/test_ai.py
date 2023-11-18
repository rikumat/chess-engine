import unittest
import chess
from services.ai import Ai



class TestAi(unittest.TestCase):
    def setUp(self):
        self.ai = Ai()

    def test_ai_valuates_development_correctly(self):
        test_position="""r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P . P P
R N B Q K B N R"""

        valuation=self.ai.evaluate(test_position, {"player_king": "e1", "ai_king": "e8"})
        self.assertGreater(-9, valuation)
        self.assertLess(-10, valuation)

    def test_ai_notices_easy_checkmate(self):
        board = chess.Board("4qk2/8/8/8/8/8/PP5R/K7 b KQkq - 0 1")
        move = self.ai.calculate_move(board, True)
        self.assertEqual(move.uci(), "e8e1")

    def test_ai_notices_medium_checkmate(self):
        board = chess.Board("r1bq2r1/b4pk1/p1pp1p2/1p2pP2/1P2P1PB/3P4/1PPQ2P1/R3K2R w")
        move = self.ai.calculate_move(board, True)
        self.assertEqual(move.uci(), "d2h6")

    def test_ai_can_solve_puzzle_1(self):
        board = chess.Board("2r3k1/p4p2/3Rp2p/1p2P1pK/8/1P4P1/P3Q2P/1q6 b - - 0 1")
        move1 = self.ai.calculate_move(board, False)
        self.assertEqual(move1.uci(), "b1g6")
        board.push(move1)
        move2=self.ai.calculate_move(board, True)
        self.assertEqual(move2.uci(), "h5g4")




