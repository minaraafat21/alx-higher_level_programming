#!/usr/bin/python3
def max_integer(my_list=[]):
    Mymax = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > Mymax:
            Mymax = my_list[i]
    if len(my_list) == 0:
        return (None)
    else:
        return Mymax
