#!/usr/bin/python3
"""The following script defines a function that determines
if a box containing a list of lists can be opened using
keys stored in the lists
"""


def canUnlockAll(boxes):
    # Initialize a set to keep track of visited boxes
    visited = set()
    # Initialize a list to keep track of boxes that need to be opened
    stack = [0]

    # Iterate through the stack
    while stack:
        # Pop a box index from the stack
        current_box = stack.pop()
        # Mark the box as visited
        visited.add(current_box)
        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # If the key corresponds to a box that hasn't been visited
            # and it's not already in the stack, add it to the stack
            if key not in visited and key not in stack and key < len(boxes):
                stack.append(key)

    # If all boxes have been visited, return True, else return False
    return len(visited) == len(boxes)
