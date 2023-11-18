import utils

import unittest
class TestUtils(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_square_to_coordinates(self):
        coordinates = utils.square_to_coordinates("h8")
        self.assertEqual(coordinates, (0, 7))
    
    def test_coordinates_to_square(self):
        square = utils.coordinates_to_square(0, 7)
        self.assertEqual(square, "h8")