#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordKeys = sorted(list(a_dictionary.keys()))
    for i in ordKeys:
        print("{}: {}".format(i, a_dictionary.get(i)))
