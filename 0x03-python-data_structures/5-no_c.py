#!/usr/bin/python3
if __name__ == "__main__":
    """printing items in list"""
    def no_c(my_string):
        str = ""
        for i in my_string:
            if i not in 'Cc':
                str += i
        return str
