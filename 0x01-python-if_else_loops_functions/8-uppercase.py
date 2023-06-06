#!/usr/bin/python3
def uppercase(s):
    for c in s:
        uppercase_c = chr(ord(c) - 32) if 'a' <= c <= 'z' else c
        print(uppercase_c, end='')
    print()
