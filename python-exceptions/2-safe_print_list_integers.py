#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    for i in range(x):
        try:
            try:
                print("{:d}".format(my_list[i]), end='')
            except (ValueError, TypeError):
                i -= 2
                pass

        except IndexError:
            IndexError("list out of range")
            raise

    print()
    return i + 1
