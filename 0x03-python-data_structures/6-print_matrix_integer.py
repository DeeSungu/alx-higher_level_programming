#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""
    for row in matrix:
        print(" ".join("{:d}".format(i) for i in row))
