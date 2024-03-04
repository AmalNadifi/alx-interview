#!/usr/bin/python3
""" The following script is for the UTF-8 Validation"""


def validUTF8(data):
    """
    This function determines if a given data set
    represents a valid UTF-8 encoding.

    Args:
        data (List[int]): The data set represented by a list of integers.
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # If this byte is part of a multibyte character
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7) != 0:
                # If the most significant bit is set, it's not a valid start byte
                return False
        else:
            # If this byte is not a continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If there are remaining bytes left
    if num_bytes != 0:
        return False

    return True
