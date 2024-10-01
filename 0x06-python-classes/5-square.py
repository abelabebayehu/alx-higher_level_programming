
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
        self.__size = size
        """gets the private attribute size"""
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """__init__

        The size setter method update the size value of the square.

        Attributes:
            size (:obj:`int`): The new size of the square.

        Raises:
            TypeError: If `size` type is not `int`.

            ValueError: If `size` is less than `0`.

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns the current square area

        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return None

        for i in range(1, self.area() + 1):
            print('#', end='')

            if i % self.__size == 0 and i > 0:
                print()
