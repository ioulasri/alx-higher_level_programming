#!/usr/bin/python3
def roman_to_int(roman_string):
    dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not roman_string or roman_string == "":
        return 0
    total = 0
    prev_value = 0
    for char in roman_string:
        if char in dictionary:
            current_value = dictionary[char]
            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value
            prev_value = current_value
        else:
            return 0
    return total

