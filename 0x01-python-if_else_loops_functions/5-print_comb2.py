#!/usr/bin/python3
for number in range(100):
    if number == 99:
        print(f"{number:d}")
    else:
        print(f"{number:02d}, ", end="")