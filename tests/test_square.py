import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_area_zero_mul(self):
        res = square.area(0)
        self.assertEqual(res, 0)
       
    def test_area_square_mul(self):
        res = square.area(12)
        self.assertEqual(res, 144)

    def test_perimeter_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter(self):
       res = square.perimeter(6)
       self.assertEqual(res, 24)
    