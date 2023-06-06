#!/usr/bin/python3
for n1 in range(10):
    for n2 in range(n1 + 1, 10):
        print("{:d}{:d}".format(n1, n2), end=", " if n1 != 8 or n2 != 9 else "\n")
