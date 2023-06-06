#!/usr/bin/python3
for c in range(97, 123):
    if c != ord('q') and chr(c) != 'e':
        print("{:c}".format(c), end="")
