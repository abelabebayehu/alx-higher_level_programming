#!/usr/bin/python3
class Square:
    """Represents a square.

    This class defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If `size` is not an integer or `position` is not a tuple of 2 positive integers.
            ValueError: If `size` is less than 0.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        if self.__check_tuple(position) is False \
           or self.__check_indexes(position) is False \
           or self.__check_integers(position) is False \
           or self.__check_values(position) is False:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.size = size
        self.position = position

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
            ValueError: If `size` is less than 0.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, position):
        """Set the position of the square.

        Args:
            position (tuple): A tuple of 2 positive integers for the square's position.

        Raises:
            TypeError: If `position` is not a tuple of 2 positive integers.
        """
        if self.__check_tuple(position) is False \
           or self.__check_indexes(position) is False \
           or self.__check_integers(position) is False \
