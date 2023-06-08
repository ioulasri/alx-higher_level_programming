#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number and list of arguments"""
    import sys

    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
