#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create an empty set to store unique elements
    unique_set = set()

    # Iterate over each element in set_1
    for element in set_1:
        # Check if the element is not present in set_2
        if element not in set_2:
            # Add the unique element to the unique_set
            unique_set.add(element)

    # Iterate over each element in set_2
    for element in set_2:
        # Check if the element is not present in set_1
        if element not in set_1:
            # Add the unique element to the unique_set
            unique_set.add(element)

    # Return the set of unique elements
    return unique_set
