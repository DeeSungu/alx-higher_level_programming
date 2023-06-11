#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Divisible by 2"""
    nlist = []
    for x in my_list:
        if x % 2 == 0:
            nlist.append(True)
        else:
            nlist.append(False)
    return nlist
