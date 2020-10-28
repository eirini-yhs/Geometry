import math
import unittest

from geometry import Circle

from geometry import Rectangle

class MyTestCase_Circle(unittest.TestCase):

    def test_something(self):
        circ = Circle(5.2)
        circ_string = str(circ)
        self.assertGreater(circ_string.find("5.2"), 0)

    def test_area_zero_radius(self):
        circ = Circle(0)
        area = circ.area()
        self.assertEqual(0, area)

    def test_area(self):
        circ = Circle(1)
        self.assertEqual(math.pi, circ.area())

    def test_circumference(self):
        circ = Circle(1)
        self.assertEqual(math.pi * 2, circ.circumference())

class MyTestCase_Rectangle(unittest.TestCase):

    def test_something2(self):
        rect = Rectangle(2, 4)
        rect_string = str(rect)
        self.assertGreater(rect_string.find("2"), 0)
        self.assertGreater(rect_string.find("4"), 0)


    def test_area_zero_rectangle(self):
        rect = Rectangle(0, 0)
        area = rect.area()
        self.assertEqual(0, area)

    def test_area(self):
        rect = Rectangle(3, 5)
        self.assertEqual(15, rect.area())

    def test_perimeter(self):
        rect = Rectangle(3, 5)
        self.assertEqual(16, rect.perimeter())
