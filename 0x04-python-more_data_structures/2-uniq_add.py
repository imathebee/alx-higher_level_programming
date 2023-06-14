#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_set = set()

    # Iterate over each element in the list
    for element in my_list:
        # Add the element to the set (duplicates will be automatically ignored)
        unique_set.add(element)

    # Compute the sum of the unique integers in the set
    sum_unique = sum(unique_set)

    # Return the sum
    return sum_unique
