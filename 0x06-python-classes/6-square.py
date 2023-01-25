#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
            postion (tuple): The position of the new square.
        """
        self.position = position
        self.size = size

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
            [print("") for _ in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(0, self.__size)]
            print("")

    @property
    def size(self):
        """Returns: size of the Square"""
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

    @property
    def position(self):
        """Returns: position of the Square"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Args:
            Value(tuple): The position of the new square.
         Raises:
            TypeError: if position is not tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
