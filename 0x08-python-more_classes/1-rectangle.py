#!/usr/bin/python3
"""
This module defines a Rectangle class that includes width and height attributes.

The Rectangle class allows for the creation of rectangle objects with specified
width and height. It includes validation checks to ensure that the width and
height are non-negative integers.
"""

class Rectangle:
    """
    An empty Rectangle class.

    This class represents a rectangle defined by its width and height.
    It provides methods to get and set these attributes while enforcing
    validation rules to maintain integrity.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with specified width and height.

        Args:
            width (int, optional): The width of the Rectangle (default is 0).
            height (int, optional): The height of the Rectangle (default is 0).
        
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.__check_valid_width(width)
        self.__check_valid_height(height)

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns the width of the Rectangle.

        Returns:
            int: The current width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle with validation.

        Args:
            value (int): The width of the Rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        self.__check_valid_width(value)
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the Rectangle.

        Returns:
            int: The current height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle with validation.

        Args:
            value (int): The height of the Rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        self.__check_valid_height(value)
        self.__height = value

    def __check_valid_width(self, width):
        """
        Validates the width to ensure it is a non-negative integer.

        Args:
            width (int): The width to validate.

        Raises:
            TypeError: If `width` is not an integer.
            ValueError: If `width` is less than 0.
        """
        if self.__check_int_value(width) is False:
            raise TypeError('width must be an integer')

        if self.__check_positive_value(width) is False:
            raise ValueError('width must be >= 0')

    def __check_valid_height(self, height):
        """
        Validates the height to ensure it is a non-negative integer.

        Args:
            height (int): The height to validate.

        Raises:
            TypeError: If `height` is not an integer.
            ValueError: If `height` is less than 0.
        """
        if self.__check_int_value(height) is False:
            raise TypeError('height must be an integer')

        if self.__check_positive_value(height) is False:
            raise ValueError('height must be >= 0')

    def __check_int_value(self, value):
        """
        Checks if the value is an integer.

        Args:
            value: The value to check.

        Returns:
            bool: True if the value is an integer, False otherwise.
        """
        return isinstance(value, int)

    def __check_positive_value(self, value):
        """
        Checks if the value is a non-negative integer.

        Args:
            value: The value to check.

        Returns:
            bool: True if the value is greater than or equal to 0, False otherwise.
        """
        return value >= 0
