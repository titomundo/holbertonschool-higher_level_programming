#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv
    n = len(args)
    result = 0

    for i in range(1, n):
        result += int(args[i])

    print(result)
