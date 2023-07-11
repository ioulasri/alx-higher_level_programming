#!/usr/bin/python3

def read_file(file=""):
    with open(file, 'r') as f:
        lines = f.readlines()
    for i in lines:
        print(i)
