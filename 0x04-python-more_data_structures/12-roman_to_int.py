#!/usr/bin/python3
def roman_to_int(roman_string):
    dictionary = {'I': 1, 'V': 5, 'X': 10,
             'L': 50, 'C': 100, 'D': 500}
    sum = 0
    i = 0
    while (i < len(roman_string)):
        o = 1
        if roman_string[i] == 'I' and i + 1 < len(roman_string):
            if roman_string[i + 1] == 'X':
                sum += 9
                i += 1
                o = 0
        elif roman_string[i] == 'I' and i + 1 < len(roman_string):
            if roman_string[i + 1] == 'V':
                sum += 4
                i += 1
                o = 0
        elif roman_string[i] == 'X' and i + 1 < len(roman_string):
            if roman_string[i + 1] == 'L':
                sum += 40
                i += 1
                o = 0
        elif roman_string[i] == 'C' and i + 1 < len(roman_string):
            if roman_string[i + 1] == 'D':
                sum += 400
                i += 1
                o = 0
        if o:
            sum += dictionary[roman_string[i]]
        i += 1
    return sum
