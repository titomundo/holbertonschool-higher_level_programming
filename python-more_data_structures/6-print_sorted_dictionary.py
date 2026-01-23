#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    arr = dict(sorted(a_dictionary.items()))
    for k, v in arr.items():
        print(f"{k}: {v}")
