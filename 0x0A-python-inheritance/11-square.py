#!/usr/bin/python3
"""a Rectangle subclass Square."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Represents a square, which is a special kind of rectangle."""
    def __init__(self, size):
           """
        Initializes a new Square instance.
        """
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
           """
           Returns the string representation of the Square instance.
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
