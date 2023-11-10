import unittest
from ..ai import Ai
import chess

class TestAi(unittest.TestCase):
    def setUp(self):
        self.ai = Ai()

    def test_ai_valuates_position_correctly(self):
        test_position="""r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B . K B N R"""
        valuation = self.ai.evaluate(test_position)
        self.assertEqual(valuation, 9)



