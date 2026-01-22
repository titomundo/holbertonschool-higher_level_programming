#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    n = len(my_list)
    arr = [False] * n

    for i in range(n):
        if my_list[i] % 2 == 0:
            arr[i] = True

    return arr
