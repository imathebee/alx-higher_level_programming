#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Variable to keep track of the number of integers printed
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")  # Print the integer
            count += 1  # Increment the count of printed integers
        except (ValueError, TypeError):  # Ignore non-integer values
            pass
        except IndexError:  # Handle index out of range exception
            break
    print()  # Print a new line
    return count  # Return the number of integers printed
