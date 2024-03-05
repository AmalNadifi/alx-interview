#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): The data set represented by a list of integers.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Initialize the number of bytes in the current UTF-8 character
    remaining_bytes = 0

    # Define bit masks for UTF-8 encoding
    start_byte_mask = 1 << 7
    cont_byte_mask = 1 << 6

    # Iterate through each byte in the data set
    for byte in data:
        # Initialize the mask byte to check the first bit
        current_mask_byte = 1 << 7

        # If this is the start byte of a UTF-8 character
        if remaining_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while current_mask_byte & byte:
                remaining_bytes += 1
                current_mask_byte = current_mask_byte >> 1

            # If the number of bytes is invalid, return False
            if remaining_bytes == 0:
                continue
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False
        else:
            # If this is a continuation byte, check its format
            if not (byte & start_byte_mask and not (byte & cont_byte_mask)):
                return False

        # Decrease the number of bytes remaining to check
        remaining_bytes -= 1

    # If all bytes have been checked and no errors found, return True
    if remaining_bytes == 0:
        return True

    # If there are remaining bytes, return False
    return False
