#!/usr/bin/python3
class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is negative.
        """
        self.size = size  # Utilize the setter for validation

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size of the square.

        Args:
            size (int): The new size of the square.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is negative.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
