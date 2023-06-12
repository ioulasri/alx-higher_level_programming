#!/usr/bin/python3
if __name__ == "__main__":
    """printing items in list"""
    def print_reversed_list_integer(my_list=[]):
        my_list = reversed(my_list)
        for i in my_list:
            print("{}".format(i))
