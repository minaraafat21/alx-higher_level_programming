#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list = my_list[:i] + [replace] + my_list[i + 1:]
    return new_list
