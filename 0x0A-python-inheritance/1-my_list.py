#!/usr/bin/python3
""" Mylist class """


class Mylist(list):
    """ Mylist class """

    def print_sorted(self):
        """ Prints the list, but sorted (ascending sort) """
        print(sorted(self))
