#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    integer = list(map(lambda char: roman.get(char, 0), roman_string))
    length = len(integer)

    for i in range(length):
        if i + 1 < length:
            if integer[i] < integer[i + 1]:
                integer[i] = -integer[i]

    return sum(integer)
