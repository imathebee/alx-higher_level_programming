#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Variable to keep track of the number of integers printed
    try:
        for i in range(x):
            if isinstance(my_list[i], int):  # Check if the element is an int
                print("{:d}".format(my_list[i]), end="")  # Print the integer
                count += 1  # Increment the count of printed integers
    except IndexError:
        pass
    print()  # Print a new line
    return count  # Return the number of integers printed
