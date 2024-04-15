#!/usr/bin/python3
""" This script defines the isWinner function,
which determines the winner in the Prime Game problem
"""

def is_prime(n):
    """This function checks if a number is prime
    Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime_numbers = []
    is_prime = [True] * (n + 1)
    for numb in range(2, n + 1):
        if is_prime[numb]:
            prime_numbers.append(numb)
            for multiple in range(numb, n + 1, numb):
                is_prime[multiple] = False
    return prime_numbers

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
    if x is None or nums is None or x == 0 or nums == []:
        return None
    maria_wins = 0
    ben_wins = 0

    # Iterate through each round
    for n in nums:
        prime = is_prime(n)
        if len(prime) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
