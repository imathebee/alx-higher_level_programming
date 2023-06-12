#!/usr/bin/python3
def element_at(my_list, idx):
    # retrieve an element from a list like in C
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
