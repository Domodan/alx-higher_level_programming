#!/usr/bin/python3
"""
find the peak in an unordered list of
integers
"""

def find_peak(list_of_integers):
    """
    Find the peak in a list of integers.
    Args:
        list_of_integers (list): List of integers.
    Returns:
        int: The peak integer(s).
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # The peak is on the left side of mid (including mid).
            right = mid
        else:
            # The peak is on the right side of mid.
            left = mid + 1

    # left is now pointing to the peak.
    return list_of_integers[left]
