import unittest
import math
import circle

class CircleTestCase (unittest.TestCase):
    def test_area_zero_mul(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    
    def test_area(self):
        res = circle.area(5)
        self.assertEqual(res, 25 * math.pi)
    
    def test_perimeter_zero_mul(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = circle.perimeter(7)
        self.assertEqual(res, 14 * math.pi)