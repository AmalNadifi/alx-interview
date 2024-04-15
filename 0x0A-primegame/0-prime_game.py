#!/usr/bin/python3
""" This script defines the isWinner function,
which determines the winner in the Prime Game problem
"""

def is_prime(num):
    """This function checks if a number is prime"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    """
    This function determines the winner of the Prime Game.

    Args:
    - x (int): Number of rounds to play.
    - nums (list): List of integers representing the starting
    numbers for each round

    Returns:
    - str or None: Name of the player with the most wins
    or None if the winner cannot be determined.
    """
    maria_wins = 0
    ben_wins = 0

    # Iterate through each round
    for n in nums:
        current_player = 0  # 0 for Maria, 1 for Ben

        # Check if the starting number is prime
        if is_prime(n):
            if current_player == 0:
                maria_wins += 1
            else:
                ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
