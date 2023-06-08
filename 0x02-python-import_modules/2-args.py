#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Print the number of and the list of its arguments."""
    argv = sys.argv[1:]  # Exclude the script name from the arguments

    num_args = len(argv)
    if num_args == 0:
        print(num_args, "arguments.")
    elif num_args == 1:
        print(num_args, "argument:")
        print("1:", argv[0])
    else:
        print(num_args, "arguments:")

        for i, arg in enumerate(argv, start=1):
            print(i, ":", arg)
