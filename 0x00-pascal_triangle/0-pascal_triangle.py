#!/usr/bin/python3
""" The following script provides a function to generate
Pascal's Triangle up to a specified number of rows.
"""

def pascal_triangle(n):
    """
    This is generating Pascal's Triangle up to the nth row.

    Args:
    - n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
    - list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    # Initialize Pascal's Triangle with the first row
    triangle = [[1]]

    # Iterate from the second row up to the nth row
    for i in range(1, n):
        # Initialize the current row with the first element
        row = [1]

        # Iterate through the inner elements of the current row
        for j in range(1, i):
            # Calculate the value by summing elements from the previous row
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)

        # Add the last element to the current row
        row.append(1)

        # Add the current row to Pascal's Triangle
        triangle.append(row)

    return triangle
