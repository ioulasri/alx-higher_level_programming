#!/usr/bin/python3
def remove_char_at(str, n):
    result = str[0:n]
    result += str[n+1:]
    return result
