#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Args:
            width (int, optional): rectangle's Width. Defaults to 0.
            height (int, optional): rectangle's Height. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for width

        Returns:
            width: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width

        Args:
            value (int): the width to be set

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height

        Returns:
            height: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height

        Args:
            value (int): the height to be set

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
