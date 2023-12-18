import unittest
from services.engine import Engine
from services.move_generator import MoveGenerator
from services.ai import Ai

move_generator = MoveGenerator()
ai = Ai(move_generator)


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
        engine = Engine(ai, move_generator, test_board)
        engine.make_move("a7a8")
        self.assertEqual(engine.board[0][0], "Q")
        engine.make_move("h2h1")
        self.assertEqual(engine.board[7][7], "q")

    def test_check_end_condition_detects_checkmate_white(self):
        test_board = [
            ["k", ".", ".", ".", ".", ".", "r", "."],
            ["P", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "P"],
            [".", ".", ".", ".", ".", ".", ".", "K"]
        ]
        engine = Engine(ai, move_generator, test_board)
        self.assertEqual(engine.check_end_condition(True), 'checkmate')

    def test_check_end_condition_detects_checkmate_black(self):
        test_board = [
            ["k", "Q", ".", ".", ".", ".", "R", "."],
            ["P", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "P"],
            [".", ".", ".", ".", ".", ".", ".", "K"]
        ]
        engine = Engine(ai, move_generator, test_board)
        self.assertEqual(engine.check_end_condition(False), 'checkmate')

    def test_check_end_condition_does_not_detect_checkmate_white(self):
        test_board = [
            ["k", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "r", ".", ".", ".", "K"]
        ]
        engine = Engine(ai, move_generator, test_board)
        self.assertEqual(engine.check_end_condition(True), False)
    
    def test_check_end_condition_does_not_detect_checkmate_black(self):
        test_board = [
            ["k", "Q", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "B", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "P"],
            [".", ".", ".", ".", ".", ".", ".", "K"]
        ]
        engine = Engine(ai, move_generator, test_board)
        self.assertEqual(engine.check_end_condition(False), False)
    
    def test_check_end_condition_detects_stalemate(self):
        test_board = [
            ["k", ".", ".", ".", ".", ".", ".", "."],
            [".", "R", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", "R", ".", ".", ".", ".", ".", "P"],
            [".", ".", ".", ".", ".", ".", ".", "K"]
        ]
        engine = Engine(ai, move_generator, test_board)
        self.assertEqual(engine.check_end_condition(False), "stalemate")

    def test_move_is_legal_notices_illegal_move_black(self):
        test_board = [
            ["k", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", "R", ".", ".", ".", ".", ".", "P"],
            [".", ".", ".", ".", ".", ".", ".", "K"]
        ]
        engine = Engine(ai, move_generator, test_board)
        legal = engine.move_is_legal("a8b8", False)
        self.assertEqual(legal, False)
    
    def test_move_is_legal_notices_illegal_move_white(self):
        test_board = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "P"],
            [".", ".", ".", "r", ".", ".", ".", "K"]
        ]
        engine = Engine(ai, move_generator, test_board)
        legal = engine.move_is_legal("h2h3", True)
        self.assertEqual(legal, False)
    
    def test_move_is_legal_does_not_alter_board(self):
        test_board = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "P"],
            [".", ".", ".", "r", ".", ".", ".", "K"]
        ]
        engine = Engine(ai, move_generator, test_board)
        legal = engine.move_is_legal("h2h3", True)
        self.assertEqual(legal, False)

        legal = engine.move_is_legal("h1h2", True)
        self.assertEqual(legal, False)


    def test_validate_move_notices_incorrect_squares(self):
        test_board = [
            ["k", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "P"],
            [".", ".", ".", "r", ".", ".", ".", "K"]
        ]
        engine = Engine(ai, move_generator, test_board)

        validity = engine.validate_move("h1h0", True)
        self.assertEqual(validity, 'Invalid move')

        validity = engine.validate_move("h1h", True)
        self.assertEqual(validity, 'Invalid move')

        validity = engine.validate_move("h1i1", True)
        self.assertEqual(validity, 'Invalid move')
    
    def test_validate_move_notices_legal_move(self):
        test_board = [
            ["k", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "P"],
            [".", ".", ".", "r", ".", ".", ".", "K"]
        ]
        engine = Engine(ai, move_generator, test_board)
        validity = engine.validate_move("h1g2", True)
        self.assertEqual(validity, True)
    
    def test_validate_move_notices_illegal_move(self):
        test_board = [
            ["k", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "P"],
            [".", ".", ".", "r", ".", ".", ".", "K"]
        ]
        engine = Engine(ai, move_generator, test_board)
        validity = engine.validate_move("h1h2", True)
        self.assertEqual(validity, "Illegal move")

        validity = engine.validate_move("h2h3", True)
        self.assertEqual(validity, "Illegal move")


    









    
    
    

    
    
    


