#!/usr/bin/python3
""" Mylist class """


class Mylist(list):
    """ Mylist class """

    def __init__(self):
        """ Constructor method """
        super().__init__()

    def print_sorted(self):
        """ Prints the list, but sorted (ascending sort) """
        print(sorted(self))
