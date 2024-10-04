"""
CS5001
HW4 - runlength_decoder
Fall 2024
Logan Matheny
"""

import hw4data

# Note the list has ints and strings


def decode(data: list) -> list:
    # Goal - make a function that takes the list and then converts it to a decoded version
    # count the number of charcaters that are the same
    # Methods
    # Pseduo
    # First character and all the odd characters represent the char to create copies of
    # Second and even characters are how many times to print it
    # Look at the first character - save it
    # Read the second character - loop and add saved value to your new decoded list
    # Add 2 to the counter and repeat
    decoded_lst = []

    for i in range(0, len(data), 2):
        secret_char = data[i]
        secret_num = data[i + 1]
        for j in range(0, secret_num):
            decoded_lst.append(secret_char)
    print(decoded_lst)


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
