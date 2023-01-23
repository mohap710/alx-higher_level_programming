#!/usr/bin/python3
""" x is a number of element to be printed from list"""


def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for el in range(x):
            print(my_list[el], end="")
            i += 1
    except IndexError:
        pass
    finally:
        print()
        return i
