#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set_1.union(set_2)
    mine = list(filter(lambda x: (x in set_1 and x not in set_2) or (x in set_2 and x not in set_1), new_set))
    return mine
