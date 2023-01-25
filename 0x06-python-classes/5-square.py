#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        Raises:
            TypeError: if size not an integer
            ValueError: if size is less than 0
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Method to calculate the area of the square
            Returns: Area of the Square
        """
        return self.__size * self.__size

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.size == 0:
            print("")
        else:
            for _ in range(self.size):
                print("#" * self.size)

    @property
    def size(self):
        """
            Returns: size of the Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args:
            Value(int): The size of the new square.
        Raises:
            TypeError: if value not an integer
            ValueError: if value is less than 0
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
