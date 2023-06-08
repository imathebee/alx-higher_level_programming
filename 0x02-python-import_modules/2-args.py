#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name from the arguments

    num_args = len(argv)
    if num_args == 0:
        print("{} argument{}.".format(num_args, "s" if num_args != 1 else ""))
    elif num_args == 1:
        print("1 argument:")
        print("1: {}".format(argv[0]))
    else:
        print("{} arguments:".format(num_args))
        for i, arg in enumerate(argv):
            print("{}: {}".format(i + 1, arg))

