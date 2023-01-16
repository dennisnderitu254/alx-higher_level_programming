#!/usr/bin/python3
""" Module that contains class Rectangle,
inheritance of class Base
"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value o y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ a function to calculate the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle"""
        rectangle = self.y * "\n"
        for i in range(self.__height):
            rectangle += (" " * self.__width)
            rectangle += ("#" * self.__width + "\n")

        print(rectangle, end="")

    def __str__(self):
        """ magic method"""
        rectangle = "[Rectangle] "
        rec_id = "({}) ".format(self.id)
        rect_xy = "{}/{} -".format(self.x, self.y)
        rec_wh = " {}/{}".format(self.width, self.height)

        return rectangle + rec_id + rect_xy + rec_wh

    def update(self, *args, **kwargs):
        """ updating class rectangle that assigns an argument"""
        count = 0
        if args is not None and len(args) != 0:
            list_arguments = ["id", "width", "height", "x", "y"]

            for values in args:
                setattr(self, list_arguments[count], values)
                count += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """method that returns a dictionary representation of a rectangle"""
        my_list = ["id", "width", "height", "x", "y"]
        dictionary = {}

        for key in my_list:
            dictionary[key] = getattr(self, key)

        return dictionary
