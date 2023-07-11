#!/usr/bin/python3
"""Module for add_item to json"""
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        my_list = load_from_json_file('add_item.json')
    except:
        my_list = []
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, 'add_item.json')
