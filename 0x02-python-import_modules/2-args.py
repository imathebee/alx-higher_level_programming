#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Print the number of and the list of its arguments."""
    argv = sys.argv[1:]  # Exclude the script name from the arguments

    num_args = len(argv)
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        print("1:", argv[0])
    else:
        print(num_args, "arguments:")
        for i in range(num_args):
            print(i + 1, ":", argv[i])
