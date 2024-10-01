#!/usr/bin/python3
"""
Square Class

This module defines a Square class that represents a square shape.
It allows the creation of square objects with a specified size.
"""

class Square:
    """
    A class that represents a square.

    This class allows the creation of square objects by defining
    their size, which is a positive integer. The class currently
    does not have any methods to manipulate the square, but it 
    serves as a foundation for further extensions.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        The __init__ method initializes the size value of the square.

        Attributes:
            size (int): The size of the square, which must be a 
                         positive integer.
        """
        self.__size = size
