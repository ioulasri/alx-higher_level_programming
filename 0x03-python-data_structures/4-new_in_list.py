#!/usr/bin/python3
if __name__ == "__main__":
    """printing items in list"""
    def new_in_list(my_list, idx, element):
        if idx < 0 or idx >= len(my_list):
            return my_list
        new_list = [i for i in my_list]
        new_list[idx] = element
        return (new_list)
