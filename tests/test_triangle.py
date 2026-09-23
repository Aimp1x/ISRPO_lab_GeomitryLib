import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_mul(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)
       
    def test_area_square_mul(self):
        res = triangle.area(10, 10)
        self.assertEqual(res, 50)

    def test_perimeter_zero(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    
    def test_perimeter(self):
       res = triangle.perimeter(10, 15, 20)
       self.assertEqual(res, 45)
    