#!/usr/bin/python3
def uppercase(s):
    for c in s:
        uppercase_c = chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c
        print("{}".format(uppercase_c), end="")
    print()
