#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv
    n = len(args)

    print(n - 1, end='')

    if n == 2:
        print(" argument:")
    else:
        print(" arguments:")

    for i in range(1, n):
        print(f"{i}: {args[i]}")
