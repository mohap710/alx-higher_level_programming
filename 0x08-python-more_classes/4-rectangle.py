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

    def area(self):
        """calculate the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """calculate the perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

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

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ""
        for i in range(self.height):
            rect += ("#" * self.width)
            if i != self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
