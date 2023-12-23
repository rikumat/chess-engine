import copy
import unittest
from services.move_generator import MoveGenerator
empty_board = [[".", ".", ".", ".", ".", ".", ".", "."][:] for x in range(8)]
class TestMoveGenerator(unittest.TestCase):
    def setUp(self):
        self.move_generator=MoveGenerator()
    
    def test_get_diagonal_moves_returns_correct_moves(self):
        test_board = [[".", ".", ".", ".", ".", ".", ".", "."][:] for x in range(8)]
    
        moves = self.move_generator.get_diagonal_moves(test_board, "a1")
        self.assertCountEqual(moves, ['a1b2', 'a1c3', 'a1d4', 'a1e5', 'a1f6', 'a1g7', 'a1h8'])

        moves = self.move_generator.get_diagonal_moves(test_board, "a2")
        self.assertCountEqual(moves, ["a2b1", "a2b3", "a2c4", "a2d5", "a2e6", "a2f7", "a2g8"])

        moves = self.move_generator.get_diagonal_moves(test_board, "b8")
        self.assertCountEqual(moves, ['b8c7', 'b8d6', 'b8e5', 'b8f4', 'b8g3', 'b8h2', "b8a7"])

        moves = self.move_generator.get_diagonal_moves(test_board, "c5")
        self.assertCountEqual(moves, ["c5d4", "c5e3", "c5f2", "c5g1", "c5d6", "c5e7", "c5f8", "c5b6", "c5a7", "c5b4", "c5a3"])

    def test_get_diagonal_moves_detects_pieces(self):
        test_board = copy.deepcopy(empty_board)
        test_board[0][0]="p"
        test_board[1][1]="q"
        test_board[2][2]="p"
        test_board[0][2]="P"
        moves = self.move_generator.get_diagonal_moves(test_board, "b7")
        self.assertCountEqual(moves, ["b7c8", "b7a6"])

        test_board = copy.deepcopy(empty_board)
        test_board[1][1] = "q"
        test_board[0][2] = "p"
        test_board[0][0] = "p"
        test_board[5][5] = "Q"

        moves = self.move_generator.get_diagonal_moves(test_board, "b7")
        self.assertCountEqual(moves, ['b7c6', 'b7d5', 'b7e4', 'b7f3', 'b7a6'])

    def test_get_vertical_and_horizontal_moves_returns_all_moves(self):
        test_board = copy.deepcopy(empty_board)
        test_board[1][1]="Q"
        moves = self.move_generator.get_vertical_and_horizontal_moves(test_board, "b7")
        self.assertEqual(moves, ["b7b8", "b7b6", "b7b5", "b7b4", "b7b3", "b7b2", "b7b1", "b7a7", "b7c7", "b7d7", "b7e7", "b7f7", "b7g7", "b7h7"])

        test_board = copy.deepcopy(empty_board)
        test_board[0][0]="Q"

        moves = self.move_generator.get_vertical_and_horizontal_moves(test_board, "a8")
        self.assertEqual(moves, ["a8a7", "a8a6", "a8a5", "a8a4", "a8a3", "a8a2", "a8a1", "a8b8", "a8c8", "a8d8", "a8e8", "a8f8", "a8g8", "a8h8"])
    
    def test_get_vertical_and_horizontal_moves_detects_pieces(self):
        test_board = copy.deepcopy(empty_board)
        test_board[1][1]="Q"
        test_board[1][5]="q"
        test_board[0][1]="P"
        test_board[7][1]="P"
        moves = self.move_generator.get_vertical_and_horizontal_moves(test_board, "b7")
        self.assertCountEqual(moves, ["b7b6", "b7b5", "b7b4", "b7b3", "b7b2", "b7a7", "b7c7", "b7d7", "b7e7", "b7f7"])

        test_board = copy.deepcopy(empty_board)
        test_board[7][7]="Q"
        test_board[7][5]="p"
        test_board[5][7]="P"

        moves = self.move_generator.get_vertical_and_horizontal_moves(test_board, "h1")
        self.assertCountEqual(moves, ["h1h2", "h1g1", "h1f1"])
    
    def test_get_knight_moves_returns_all_moves(self):
        test_board = copy.deepcopy(empty_board)
        moves = self.move_generator.get_knight_moves(test_board, "g1")
        self.assertCountEqual(moves, ["g1f3", "g1e2", "g1h3"])

        moves2 = self.move_generator.get_knight_moves(test_board, "f6")
        self.assertCountEqual(moves2, ["f6h7", "f6h5", "f6g8", "f6e8", "f6g4", "f6e4", "f6d5", "f6d7"])
    
    def test_get_pawn_moves_returns_all_moves(self):
        test_board = copy.deepcopy(empty_board)
        test_board[5][5]="P"
        test_board[5][7]="P"
        test_board[4][4]="p"
        test_board[4][6]="p"

        moves = self.move_generator.get_pawn_moves(test_board, "f3")
        self.assertCountEqual(moves, ["f3f4", "f3e4", "f3g4"])

        moves = self.move_generator.get_pawn_moves(test_board, "g4")
        self.assertCountEqual(moves, ["g4f3", "g4g3", "g4h3"])
    
    def test_get_pawn_moves_notices_pieces(self):
        test_board = copy.deepcopy(empty_board)
        test_board[5][5]="P"
        test_board[4][5]="P"
        test_board[4][4]="P"
        test_board[4][6]="p"
        test_board[5][6]="p"
        for i in test_board:
            print(i)
        moves = self.move_generator.get_pawn_moves(test_board, "f3")
        self.assertCountEqual(moves, ["f3g4"])

        moves = self.move_generator.get_pawn_moves(test_board, "g4")
        self.assertCountEqual(moves, ["g4f3"])
    
    def test_get_king_moves_gets_all_moves(self):
        test_board = copy.deepcopy(empty_board)
        moves = self.move_generator.get_king_moves(test_board, "f3")
        self.assertCountEqual(moves, ['f3g2', 'f3e2', 'f3f2', 'f3g4', 'f3e4', 'f3f4', 'f3g3', 'f3e3'])

        moves = self.move_generator.get_king_moves(test_board, "h1")
        self.assertCountEqual(moves, ['h1g2', 'h1h2', 'h1g1'])
    
    def test_get_king_moves_detects_pieces(self):
        test_board = copy.deepcopy(empty_board)
        test_board[0][0]="K"
        test_board[1][1]="P"
        moves = self.move_generator.get_king_moves(test_board, "a8")
        self.assertCountEqual(moves, ["a8a7", "a8b8"])

        test_board = copy.deepcopy(empty_board)
        test_board[5][5]="k"
        test_board[4][5]="p"
        test_board[6][5]="p"
        test_board[5][6]="p"
        test_board[5][4]="p"
        test_board[4][4]="Q"

        moves = self.move_generator.get_king_moves(test_board, "f3")
        self.assertCountEqual(moves, ['f3g2', 'f3e2', 'f3g4', 'f3e4'])

    def test_get_all_moves_returns_all_moves(self):
        test_board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "P", ".", ".", "."],
            ["P", "P", "P", "P", ".", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        moves = self.move_generator.get_moves_from_board(test_board, False)
        self.assertCountEqual(moves, ['b8a6',
                                'b8c6',
                                'g8f6',
                                'g8h6',
                                'a7a5',
                                'a7a6',
                                'b7b5',
                                'b7b6',
                                'c7c5',
                                'c7c6',
                                'd7d5',
                                'd7d6',
                                'e7e5',
                                'e7e6',
                                'f7f5',
                                'f7f6',
                                'g7g5',
                                'g7g6',
                                'h7h5',
                                'h7h6'])
        

