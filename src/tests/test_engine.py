import unittest
from ..engine import Engine
import chess

class TestEngine(unittest.TestCase):
    def setUp(self):
        self.engine=Engine(chess.Board())

    def test_make_move_updates_board_correctly(self):
        self.engine.make_move("e2e4")
        self.assertEqual(str(self.engine.get_board()), """r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . P . . .
. . . . . . . .
P P P P . P P P
R N B Q K B N R""")
