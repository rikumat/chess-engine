import unittest
from services.engine import Engine

class TestEngine(unittest.TestCase):
    def setUp(self):
        pass

    def test_make_move_updates_board_correctly(self):
        test_board = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."]
        ]
        engine = Engine(test_board)
        engine.make_move("a7a8")
        self.assertEqual(engine.board[0][0], "Q")
        engine.make_move("h2h1")
        self.assertEqual(engine.board[7][7], "q")
    


