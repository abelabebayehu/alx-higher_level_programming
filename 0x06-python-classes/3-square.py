#!/usr/bin/python3
class Square:
    """Square Class

    This class defines a square by its size and provides a method
    to calculate the area of the square.
    """

    def __init__(self, size=0):
        """Initialize a Square instance.

        The __init__ method initializes the size of the square.

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
        """Calculate the area of the square.

        Returns:
            int: The area of the square, calculated as size squared.
        """
        return self.__size ** 2
