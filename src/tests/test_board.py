import unittest
from entities.board import Board
class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board=Board()
    
    def test_get_diagonal_moves_returns_correct_moves(self):
        test_board=[
            ".Q......",
            "........",
            "........",
            "........",
            "........",
            "........",
            "........",
            "........",
        ]
        b8 = self.board.get_diagonal_moves(test_board, "b8")
        self.assertEqual(b8, ['c7', 'd6', 'e5', 'f4', 'g3', 'h2'])

        a1 = self.board.get_diagonal_moves(test_board, "a1")
        self.assertEqual(a1, [])

        a2 = self.board.get_diagonal_moves(test_board, "a2")
        self.assertEqual(a2, ["b1"])