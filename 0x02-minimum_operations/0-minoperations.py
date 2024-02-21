#!/usr/bin/python3
"""
The following script is a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    This function calculates the min number of operations
    to reach 'n' H characters

    Args:
    n (int): The target number of H characters.

    Returns:
    int: The minimum number of operations needed.

    If 'n' is impossible to achieve, return 0.
    """

    # If n is non-positive, return 0
    if n <= 0:
        return 0
    # Initializing variables
    operations = 0    # Total number of operations
    clipboard = 1     # Number of H characters in the clipboard
    total_h = 1       # Total number of H characters in the file

    # Continue operations until total_h reaches or exceeds n
    while total_h < n:
        # If n is divisible by total_h, update clipboard & count this operation
        if n % total_h == 0:
            clipboard = total_h
            operations += 1
        # Add clipboard to total_h (paste) and count this operation
        total_h += clipboard
        operations += 1

    return operations
