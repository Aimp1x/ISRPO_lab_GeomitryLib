import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_area_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
       
    def test_area_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_perimeter_zero(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)
    
    def test_perimeter(self):
       res = rectangle.perimeter(10, 15)
       self.assertEqual(res, 50)
    