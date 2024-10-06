"""
CS5001
HW4 - mbta.py
Fall 2024
Logan Matheny
"""

import mbta_data
import copy

T_LINES = mbta_data.T_LINES
WORKING_LINES = mbta_data.WORKING_LINES


def preprocess_data():
    """
    Function: Mutate the WORKING_LINES list to create list with
    all upper case elements
    Return: List of lists with uppercase elements
    """
    # I want to iterate thru two shallow copies
    # Change to uppercase and then append them
    for single_line in T_LINES:
        single_t_line = []

        for station in single_line:
            single_t_line.append(station.upper())

        WORKING_LINES.append(single_t_line)


def is_valid_station(station, line):
    """
    Function: Takes in station and line arguments and assesses if a
    given station is on a particular line
    Return: Boolean based on station's presence on given line
    >>> is_valid_station(RED, ASHMONT)
    True
    """

    # I could make a dictionary of the lines based on the [0] index of
    # each list?
    # otherwise I could iterate through once, check the first term for a match
    # then when a match is found check to see if the station is in there

    for t_line in WORKING_LINES:
        if line in t_line:
            if station in t_line:
                return True
            else:
                return False
        else:
            continue

    return False


def get_num_stops(start, end, line):
    """Function get_num_stops
    Input: two T stations (must be on the same line), strings
    Returns: number of stops between the two, a positive integer
    """


def get_direction(start, end, line):
    """Function get_destination
    Input: start and end stations (both strings), and a line (string)
    Returns: the final stop in the direction
    from start to end (a string)

    Does: Finds the line both stops are on.
    Counts the number of stops from start to end.
    If it's negative, return the first station from that
    line, otherwise return the final station.
    If the line is invalid or not found, return a string "line not found"
    If the destination or start is not found, return "no destination found"
    """


def main():
    preprocess_data()
    print(WORKING_LINES)


if __name__ == "__main__":
    main()
