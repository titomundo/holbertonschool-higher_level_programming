#!/usr/bin/python3

def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number, prev = 0, 1000

    for i in range(len(roman_string)):
        cur = roman.get(roman_string[i])

        if prev < cur:
            number -= (prev * 2)

        number += cur
        prev = cur

    return number
