#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (float or int, optional): The size of the square. Default is 0.
        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Parameters:
            value: The size to be set.
        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison method for squares based on area.

        Parameters:
            other (Square): The other square to compare.
        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparison method for squares based on area.

        Parameters:
            other (Square): The other square to compare.
        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Greater than comparison method for squares based on area.

        Parameters:
            other (Square): The other square to compare.
        Returns:
            bool: True if area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal comparison method for squares based on area.

        Parameters:
            other (Square): The other square to compare.
        Returns:
            bool: True if area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Less than comparison method for squares based on area.

        Parameters:
            other (Square): The other square to compare.
        Returns:
            bool: True if area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal comparison method for squares based on area.

        Parameters:
            other (Square): The other square to compare.
        Returns:
            bool: True if area is less or equal, False otherwise.
        """
        return self.area() <= other.area()
