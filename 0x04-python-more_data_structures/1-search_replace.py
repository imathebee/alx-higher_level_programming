#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified values
    replaced_list = []

    # Iterate over each element in the original list
    for element in my_list:
        # Check if the element matches the search value
        if element == search:
            # If so, replace it with the new value
            replaced_list.append(replace)
        else:
            # Otherwise, keep the original value
            replaced_list.append(element)

    # Return the replaced list
    return replaced_list
