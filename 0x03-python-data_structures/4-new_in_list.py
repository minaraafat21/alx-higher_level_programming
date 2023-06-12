#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx not in range(len(my_list)):
        return my_list
    else:
        duplist = my_list[:]
        duplist[idx] = element
        return duplist
