#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = list(filter(lambda x: x in set_1 and x in set_2, set_1))
    return common
