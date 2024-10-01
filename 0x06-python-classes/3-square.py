#!/usr/bin/python3
"""
Square Class

This module defines a Square class that represents a square shape.
It allows the creation of square objects with a specified size, 
with validation to ensure the size is a non-negative integer.
"""

class Square:
    """
    A class that represents a square.

    This class allows the creation of square objects by defining
    their size, which must be a non-negative integer. The class
    raises exceptions for invalid size inputs.

    Attributes:
        __size (int): The size of the square, which must be a 
                      non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance.

        The __init__ method initializes the size value of the square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If `size` is not of type `int`.
            ValueError: If `size` is less than `0`.

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

def area(self):
    """ this method returns the square area """
    return self.__size ** 2
