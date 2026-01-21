#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    values = [0, 0, 0, 0]

    if len(tuple_a) < 2:
        for i in range(len(tuple_a)):
            values[i] = tuple_a[i]
    else:
        values[0] = tuple_a[0]
        values[1] = tuple_a[1]

    if len(tuple_b) < 2:
        for i in range(len(tuple_b)):
            values[i + 2] = tuple_b[i]
    else:
        values[2] = tuple_b[0]
        values[3] = tuple_b[1]

    tuple = values[0] + values[2], values[1] + values[3]

    return tuple
