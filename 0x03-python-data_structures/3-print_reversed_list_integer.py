#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """print list in reverse order"""
    if isinstance(my_list, list):
        for x in reversed(my_list):
            print("{:d}".format(x))
