#!/usr/bin/python3
"""
    N-Queen Problem Solver
    This algorithm solves the N-Queen problem
    for any given N x N chessboard, where N > 3.
"""

import sys


def n_queen_solution(temp_arr, solutions, col_occupied, row, n):
    """
    Find all possible solutions for the N-Queen problem
    and return them in a list.

    Args:
        temp_arr (list): Temporary list to store all points
        of a possible solution.

        solutions (list): Store all solutions found.

        col_occupied (list): Stores the columns used by queens
        in a given solution.

        row (int): The current row of the chessboard.

        n (int): Number of queens.

    Returns:
        list: List containing all possible solutions for the N-Queen problem.
    """
    if row > n:
        solutions.append(temp_arr[:])
        return solutions

    for col in range(n + 1):
        if row == 0 or ([row - 1, col - 1] not in temp_arr and
                        [row - 1, col + 1] not in temp_arr and
                        col not in col_occupied):
            if row > 1:
                diagonal = 0
                for k in range(2, row + 1):
                    if ([row - k, col - k] in temp_arr) or \
                            ([row - k, col + k] in temp_arr):
                        diagonal = 1
                        break
                if diagonal:
                    continue
            temp_arr.append([row, col])
            col_occupied.append(col)
            n_queen_solution(temp_arr, solutions, col_occupied, row + 1, n)
            col_occupied.pop()
            temp_arr.pop()

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    n_queen_arr = n_queen_solution([], [], [], 0, n - 1)
    for solution in n_queen_arr:
        print(solution)
