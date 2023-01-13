#!/usr/bin/python3
def weight_average(my_list=[]):
    # sum: of weight , tuple first element * second elemnts
    # div: sum of weight from all tuples (second element)
    sum = 0
    div = 0
    if len(my_list) == 0:
        return 0
    for el in my_list:
        sum += el[0] * el[1]
        div += el[1]
    return sum / div
