from services.engine import Engine
from services.move_generator import MoveGenerator
from services.ai import Ai
import unittest

move_generator = MoveGenerator()
ai=Ai(MoveGenerator())

class TestIntegration(unittest.TestCase):
    def setUp(self):
            self.board = MoveGenerator()
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
        engine = Engine(ai, move_generator, test_board)
        value, move = ai.calculate_move(engine.board, False)
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
        engine=Engine(ai, move_generator, test_board)
        ai.calculate_move(engine.board, False)
        self.assertEqual(engine.board[4][3], "P")

    def test_ai_notices_blunder_3(self):
        test_board = [
            [".", ".", ".", "k", ".", ".", ".", "."],
            [".", ".", "R", ".", ".", ".", ".", "."],
            [".", "P", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", "N", ".", ".", "."],
            [".", ".", ".", "P", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "K"]
        ]
        engine = Engine(ai, move_generator, test_board)
        value, move = ai.calculate_move(test_board, False)
        self.assertEqual(move, "d6c7")

    def test_ai_notices_blunder_4(self):
        empty_board = [
            [".", "K", ".", "R", ".", ".", ".", "R"],
            ["P", "P", "P", ".", ".", "P", "P", "P"],
            [".", ".", "B", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "q", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", ".", ".", ".", "p", "p"],
            ["r", ".", "b", "k", ".", ".", ".", "r"]
        ]
        test_board = [x[::-1] for x in empty_board[::-1]]
        engine = Engine(ai, move_generator, test_board)
        value, move = ai.calculate_move(engine.board, False)
        self.assertEqual(move, "d5e6")
    
    def test_ai_notices_blunder_4(self):
        empty_board = [
            [".", "K", ".", "R", ".", ".", ".", "R"],
            ["P", "P", "P", ".", ".", "P", "P", "P"],
            [".", ".", "B", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "q", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", ".", ".", ".", "p", "p"],
            ["r", ".", "b", "k", ".", ".", ".", "r"]
        ]
        test_board = [x[::-1] for x in empty_board[::-1]]
        engine = Engine(ai, move_generator, test_board)
        value, move = ai.calculate_move(engine.board, False)
        self.assertEqual(move, "d5e6")

    def test_ai_notices_blunder_5(self):
        test_board = [
                ["R", ".", "B", "K", ".", "R", ".", "."],
                ["P", "P", "P", ".", ".", "P", "P", "P"],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "r", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "P", "k", "N", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."]
            ]
        test_board= [x[::-1] for x in test_board[::-1]]
        value, move = ai.calculate_move(test_board, False)
        self.assertIn(move, ["d7e7", "b5e5"])

        
