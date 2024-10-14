#!/usr/bin/python3
"""
Import the BaseGeometry class from a module named '7-base_geometry'.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class to represent a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        
        Validates that both width and height are integers greater than zero.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Private attributes to store the dimensions of the rectangle
        self.__width = width
        self.__height = height
