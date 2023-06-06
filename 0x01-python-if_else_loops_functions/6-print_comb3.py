#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i == 8 and j == 9:
            print(f"{i:d}{j:d}")
        elif i != j and j > i:
            print("{:d}{:d}, ".format(i, j), end="")
