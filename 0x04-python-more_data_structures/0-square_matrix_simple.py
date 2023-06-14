#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    squared_matrix = []

    # Iterate over each row in the matrix
    for row in matrix:
        # Create a new row to store the squared values
        squared_row = []

        # Iterate over each element in the row and compute its square
        for element in row:
            squared_element = element ** 2
            squared_row.append(squared_element)

        # Append the squared row to the squared matrix
        squared_matrix.append(squared_row)

    # Return the squared matrix
    return squared_matrix
