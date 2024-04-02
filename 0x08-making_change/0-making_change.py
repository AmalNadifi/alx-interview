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

    # Initialize a list to store the minimum number of coins needed
    # for each amount from 0 to total
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for amount 0
    dp[0] = 0

    # Iterate through each amount from 1 to total
    for amount in range(1, total + 1):
        # Iterate through each coin value in coins
        for coin in coins:
            if coin <= amount:
                # Update the minimum number of coins needed
                # for the current amount
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still float('inf'), it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
