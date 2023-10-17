#!/usr/bin/python3
'''Rectangle Module'''
Base = __import__("base").Base


class Rectangle(Base):
    '''Rectangle Class that enherit from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Init Method for Rectangle Class

        Args:
            -width: width of Rectangle
            -width: width of Rectangle
            -x: int arg
            -y: int arg
        '''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''width Getter'''
        return self.__width

    @width.setter
    def width(self, width):
        '''width Setter'''
        self.__width = width

    @property
    def height(self):
        '''height Getter'''
        return self.__height

    @height.setter
    def height(self, height):
        '''height Setter'''
        self.__height = height

    @property
    def x(self):
        '''x Getter'''
        return self.__x

    @x.setter
    def x(self, x):
        '''x Setter'''
        self.__x = x

    @property
    def y(self):
        '''y Getter'''
        return self.__y

    @y.setter
    def y(self, y):
        '''y Setter'''
        self.__y = y
