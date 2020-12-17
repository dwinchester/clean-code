import unittest
from src.points import Point


class TestPoint(unittest.TestCase):
    def test_coordinate_values(self):
        point = Point(50, 100)
        self.assertEqual(point.x, 50)
        self.assertEqual(point.y, 100)
