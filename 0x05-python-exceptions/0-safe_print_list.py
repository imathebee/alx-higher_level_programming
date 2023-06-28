#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # Counter variable to keep track of elements printed

    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass  # Ignore index errors if x is greater than the length of my_list

    print()  # Print a new line after printing the elements
    return count
