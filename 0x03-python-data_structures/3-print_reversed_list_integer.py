#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Get the reversed version of the list
    new_list = my_list[::-1]
    
    # Iterate over the elements and print them
    for element in new_list:
        print("{:d}".format(element))
