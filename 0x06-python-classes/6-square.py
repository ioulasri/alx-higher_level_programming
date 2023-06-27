#!/usr/bin/python3
""" define a class Square"""


class Square():
    """ the class square """
    def __init__(self, __size=0, __position=(0, 0)) -> None:
        if type(__size) != int:
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size
        if type(__position) != tuple and __position[0] > 0 and __position[1] > 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = __position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple and value[0] > 0 and value[1] > 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        [print() for i in range(0, self.__position[1])]
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print()
