import utils

import unittest
class TestUtils(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_square_to_coordinates(self):
        coordinates = utils.square_to_coordinates("h8")
        self.assertEqual(coordinates, (0, 7))
