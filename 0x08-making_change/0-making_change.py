#!/usr/bin/python3
"""
This is the module for making change using the fewest number of coins
"""


def makeChange(coins, total):
    """
    This function determines the fewest number of coins
    needed to meet a given amount total.

    Args:
    - coins (list): A list of coin values available.
    - total (int): The total amount to make change for.

    Returns:
    - int: The fewest number of coins needed to meet the total amount.
           Return -1 if the total cannot be met by any combination of coins.
    """
    if total <= 0:
        return 0

    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coin_counter = 0
    for i in coins:
        if total % i == 0:
            coin_counter += int(total / i)
            return coin_counter
        if total - i >= 0:
            if int(total / i) > 1:
                coin_counter += int(total / i)
                total = total % i
            else:
                coin_counter += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_counter
