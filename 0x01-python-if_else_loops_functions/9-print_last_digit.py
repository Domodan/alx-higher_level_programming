#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        last = number % 10
    else:
        last = -1 * (number % -10)
    print(f"{last:d}", end="")
    return last
