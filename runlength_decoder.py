"""
CS5001
HW4 - runlength_decoder
Fall 2024
Logan Matheny
"""

import hw4data

# Note the list has ints and strings

# Goal - make a function uses a coded version of chars to create
# a decoded version


def decode(data: list) -> list:
    """
    Function: Takes in a list argument of unspecified length and uses
        it as a code to create a new decoded list
    Returns: A decoded list of characters
    >>> decode(coded_list)
    [P, P, P, Y, Y, T, H, H, O, N, N]

    """
    # Generate list to 'hold' characters
    decoded_lst = []

    # Create loop that will
    # Go through length of 'coded' data
    # Identify the letter and number of times to be printed
    for i in range(0, len(data), 2):
        secret_char = data[i]
        secret_num = data[i + 1]

        # Loop through and append char to the decoded list
        for j in range(0, secret_num):
            decoded_lst.append(secret_char)
    return decoded_lst


def main():
    decode(hw4data.DATA0)


# print(decode(hw4data.DATA0))
# print(decode(hw4data.DATA1))
# print(decode(hw4data.DATA2))
# print(decode(hw4data.DATA3))
# print(decode(hw4data.DATA4))
# print(decode(hw4data.DATA5))


if __name__ == "__main__":
    main()
