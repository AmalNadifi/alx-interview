#!/usr/bin/python3
"""
The following script is for a function that rotates an nxn 2D matrix
90 degrees clockwise in-place
"""


def rotate_2d_matrix(matrix):
    """
    This is the function that rotates a 2D matrix 90 degrees clockwise inplace

    Args:
    - matrix (list of lists): The input 2D matrix to rotate.

    Returns:
    - None. The matrix is edited in-place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            # Swap elements across the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to get the clockwise rotation
    for row in matrix:
        row.reverse()
