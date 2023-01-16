#!/usr/bin/python3
"""creating a class square that inherits from class rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ __str__ magic method"""
        square = "[Square] "
        square_id = "({}) ".format(self.id)
        square_xy = "{}/{} - ".format(self.x, self.y)
        square_size = "{}".format(self.width)

        return square + square_id + square_xy + square_size

    @property
    def size(self):
        """getting the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """setting the value of the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ creating the update function"""

        count = 0
        if args is not None and len(args) != 0:
            argument_list = ["id", "size", "x", "y"]
            for values in args:
                if argument_list[count] == "size":
                    setattr(self, "width", values)
                    setattr(self, "height", values)
                else:
                    setattr(self, argument_list[count], values)
                count += 1
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ method to return a square to a dictionary"""
        my_list = ["id", "size", "x", "y"]
        dictionary = {}

        for value in my_list:
            if value == 'size':
                dictionary[value] = getattr(self, 'width')
            else:
                dictionary[value] = getattr(self, value)

        return (dictionary)
