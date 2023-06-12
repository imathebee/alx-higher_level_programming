#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Get the first two integers from each tuple or use 0 for missing values
    a = tuple_a[0] if len(tuple_a) > 0 else 0
    b = tuple_a[1] if len(tuple_a) > 1 else 0
    c = tuple_b[0] if len(tuple_b) > 0 else 0
    d = tuple_b[1] if len(tuple_b) > 1 else 0

    # Perform addition
    result = (a + c, b + d)
    return result
