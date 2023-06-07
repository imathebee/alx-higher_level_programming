#!/usr/bin/python3
for c in range(ord('z'), ord('A') - 1, -1):
    print(chr(c) if (ord('z') - c) % 2 == 0 else chr(c - 32), end='')
