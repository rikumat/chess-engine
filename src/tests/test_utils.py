import utils

import unittest
class TestUtils(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_square_to_coordinates(self):
        h8 = utils.square_to_coordinates("h8")
        self.assertEqual(h8, (0, 7))

        b4=utils.square_to_coordinates("b4")
        self.assertEqual(b4, (4, 1))
    
    def test_coordinates_to_square(self):
        h8 = utils.coordinates_to_square((0, 7))
        self.assertEqual(h8, "h8")

        b4=utils.coordinates_to_square((4, 1))
        self.assertEqual(b4, "b4")