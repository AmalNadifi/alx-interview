#!/usr/bin/python3
"""This module calculates the perimeter of the island described in the grid"""


def island_perimeter(grid):
    """
    This function calculates the perimeter of the island described in the grid.

    Args:
    - grid (List[List[int]]): A grid representing the island,
    where 0 represents water and 1 represents land.

    Returns:
    - int: The perimeter of the island.

    Constraints:
    - The grid is rectangular with width and height not exceeding 100.
    - The grid is completely surrounded by water.
    - There is only one island (or nothing).
    - The island doesn’t have “lakes” (water inside that isn’t connected
    to the water surrounding the island).
    - Cells are connected horizontally/vertically (not diagonally)
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4  # Add 4 for each land cell
                if i > 0 and grid[i - 1][j] == 1:
                    # Minus 2 if neighboring cell is also land(horizontalcheck)
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    # Minus 2 if neighboring cell is also land(vertital check)
                    perimeter -= 2
    return perimeter
