#!/usr/bin/python3
def weight_average(my_list=[]):
    wei = 0
    average = []
    for tuple in my_list:
        average.append(tuple[1])
        wei += tuple[0] * tuple[1]
    return wei / sum(average)
