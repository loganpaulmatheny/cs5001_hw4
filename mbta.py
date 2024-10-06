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
    # Iterate through lines of the list of lines and create a 'holder' list
    for single_line in T_LINES:
        single_t_line = []

        # Iterate through line header and stations and change to uppercase
        # Append the new line to WORKING_LINES
        for station in single_line:
            single_t_line.append(station.upper())

        WORKING_LINES.append(single_t_line)


def is_valid_line(line):
    """
    Function: Determines if a given line is valid
    Returns: Boolean if the line is valid in the set
    >>> is_valid_line("ORANGE")
    True
    """
    # Iterate through lines within the WORKING_LINES constant
    # If the line is found in a nested string, return true
    for mbta_line in WORKING_LINES:
        if line in mbta_line:
            return True
        else:
            continue
    return False


def is_valid_station(station, line):
    """
    Function: Takes in station and line arguments and assesses if a
    given station is on a particular line
    Return: Boolean based on station's presence on given line
    >>> is_valid_station(RED, ASHMONT)
    True
    """

    # Similar to is_valid_line() just one extra step of once the line is found
    # You must see if the station is in that particular line list
    for t_line in WORKING_LINES:
        if line in t_line:
            if station in t_line:
                return True
            else:
                return False
        else:
            continue

    return False


def check_same_stop(start, stop):
    """
    Function: Takes two stations as arguments and sees if they are
    the same stop
    Return: Boolean, NOTE - if True then the stops are different
    >>> check_same_stop("HAYMARKET", "HAYMARKET")
    False
    """
    if start == stop:
        return False
    else:
        return True


def get_num_stops(start, end, line, direction=False):
    """
    Function: Given two stations, the line, and optional direction as args.
    will return the number of stops between two stations
    Additional Notes: If direction is true, it will give either a
    positive (meaning the train is moving towards end of line) or
    negative (meaning the train is movine towards start of line) int
    Returns: number of stops between the two stations
    >>> get_num_stops("STONY BROOK", "DOWNTOWN CROSSING", "ORANGE")
    8
    """
    # Check to ensure stops are not the same stop and line/stations valid
    # Then similar to validating line/stations iterate through list
    if (
        check_same_stop(start, end)
        and is_valid_line(line)
        and is_valid_station(start, line)
        and is_valid_station(end, line)
    ):
        for single_line in WORKING_LINES:
            # When the correct line is found, index the positions of start/end
            # Find the difference between index points
            if line in single_line:
                starting_station = single_line.index(start)
                ending_station = single_line.index(end)

                stops = ending_station - starting_station

        # To be used in get_directions, this allows you to return the direction
        # when desired
        if direction is False:
            return abs(stops)

        elif direction:
            return stops

    else:
        return 0


def find_line(line):
    """
    Function: Helper function to make a copy of a line
    Returns: A line list or if no line exists it will return a string for
    debugging
    """
    for single_line in WORKING_LINES:
        if line in single_line:
            return copy.copy(single_line)

        else:
            continue
    return "didn't find that line"


def get_direction(start, end, line):
    """
    Function: Takes starting and ending stations as well as line as
    arguments. Will be used to help the user get on the right train
    as trains are usually named with the last stop in a given direction
    Return: Either strings to the user signifying that no station or line was
    found OR the name of the stop the user is attempting to head towards with
    given start, end, and line arguments
    >>> get_direction("STONY BROOK", "DOWNTOWN CROSSING", "ORANGE")
    NORTH STATION
    """

    # Check that the line is valid and return string if invalid
    # Check if stations are on the given line if invalid print string
    if is_valid_line(line):
        if is_valid_station(start, line) and is_valid_station(end, line):
            # Get the number of stops between stations AND DIRECTION
            direction = get_num_stops(start, end, line, True)

            # Make a copy of the list of stations for that line
            # Based on the direction, return either the first or last stops
            # on the line
            line = find_line(line)
            if direction > 0:
                return line[-1]
            else:
                return line[1]

        else:
            return "no destination found"
    else:
        return "line not found"


def main():
    print("HW 4 Completed!")


if __name__ == "__main__":
    main()
