#!/usr/bin/python3
"""Rectangle Module"""
Base = __import__("base").Base


class Rectangle(Base):
    """
    Rectangle Class that inherits from Base.

    Arguments:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        - x (int): Horizontal position.
        - y (int): Vertical position.
        - id: Identifier.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width Getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width Setter"""
        if type(width) is not int:
            raise TypeError(f"width must be an integer")
        elif width <= 0:
            raise ValueError(f"width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """height Getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height Setter"""
        if type(height) is not int:
            raise TypeError(f"height must be an integer")
        elif height <= 0:
            raise ValueError(f"height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """x Getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x Setter"""
        if type(x) is not int:
            raise TypeError(f"x must be an integer")
        elif x < 0:
            raise ValueError(f"x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """y Getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y Setter"""
        if type(y) is not int:
            raise TypeError(f"y must be an integer")
        elif y < 0:
            raise ValueError(f"y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """Area method"""
        return self.__height * self.__width

    def display(self):
        """print to stdout"""
        print("\n"*self.__y, end='')
        for i in range(self.__height):
            print(" "*self.__x, end='')
            for j in range(self.__width):
                print("#", end='')
            print("\n", end='')

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Format:
        "[Rectangle] (id) x/y - width/height"
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "\
               f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update method"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
