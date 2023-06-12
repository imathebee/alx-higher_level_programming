#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Get the length of the list
    length = len(my_list)

    # Iterate over the indices in reverse order
    for i in range(length - 1, -1, -1):
        # Print the integer using str.format()
        print("{:d}".format(my_list[i]))
