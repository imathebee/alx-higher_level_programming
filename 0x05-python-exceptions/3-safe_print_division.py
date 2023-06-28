#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b  # Perform the division
    except ZeroDivisionError:
        result = None  # If b is 0, set result to None
    finally:
        print("Inside result: {}".format(result))  # Print res in finally block
    return result
