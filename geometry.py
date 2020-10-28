"""
Geometry module provides classes to help determine geometric calculations
"""

import math

class Circle:
    def __init__(self, radius: float):
        """
        Constructor
        :param radius:  non-negative number (if a negative number is passed, it will be converted to a positive number)
        """
        self.radius = radius


    def __str__(self) -> str:
        """
        Formats a string showing the attributes of the Circle
        :return: formatted string
        """
        return f"Circle with radius {self.radius}"

    def area(self) -> float:
        """
        Calculates the area of the circle
        :return: non-negative number
        """
        return math.pi * (self.radius ** 2)


    def circumference(self) -> float:
        """
        Calculates the perimeter of the circle
        :return: non-negative number
        """
        return (2 * math.pi * self.radius)




class Rectangle:
    pass


    def __init__(self, length, width: float):
        """
        Constructor
        :param radius:  non-negative number (if a negative number is passed, it will be converted to a positive number)
        """
        self.length = length
        self.width = width

    def __str__(self) -> str:
        """
        Formats a string showing the attributes of the Circle
        :return: formatted string
        """
        return f"Rectangle with length {self.length} and with width {self.width}"


    def area(self) -> float:
        """
        Calculates the area of the circle
        :return: non-negative number
        """
        return (self.length * self.width)


    def perimeter(self) -> float:
        """
        Calculates the perimeter of the circle
        :return: non-negative number
        """
        return (self.length * 2 + self.width * 2)
