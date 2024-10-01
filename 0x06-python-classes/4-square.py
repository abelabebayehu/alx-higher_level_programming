#!/usr/bin/python3
class Square:
    """Square Class

    This class defines a square by its size and provides methods to 
    calculate its area and manage the size attribute.
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
        self.size = size  # Utilize the setter for validation

    @property
    def size(self):
        """Get the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size of the square.

        This method sets the size of the square, ensuring that it
        is a non-negative integer.

        Args:
            size (int): The new size of the square.

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
