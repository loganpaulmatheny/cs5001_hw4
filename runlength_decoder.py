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
    # Create a value holder, and an occurance holder
    # Read the character if it's different than holder, change value holder to character and change occurance count to one
    # Check next character if it's the same add to occurance count
    # If you get a new character
    # Add the previous to your decoded list and then
    # Change occurence value, reset the count to 1
    # Loop until your done with the length of the data

    value_holder = data[0]
    print(value_holder)
    occurrence_holder = 0

    decoded_list = []

    for i in data:
        if data[i] == value_holder:
            occurrence_holder += 1
        else:
            decoded_list.append(value_holder)
            decoded_list.append(occurrence_holder)

            value_holder = data[i]
            occurrence_holder = 1

    return decoded_list
    print(decoded_list)


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
