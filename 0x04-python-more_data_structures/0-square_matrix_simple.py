#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    print([list(map(lambda x: x * x, row)) for row in matrix])
