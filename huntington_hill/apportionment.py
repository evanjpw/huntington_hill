"""
A Python 3 implementation of the Huntington–Hill method
of equal proportions for congressional apportionment.
"""

import collections
from math import sqrt
from typing import Dict, OrderedDict


def calculate_apportionment(census_data: Dict, num_seats: int) -> OrderedDict:
    """

    :param census_data:
    :param num_seats:
    :return:
    """
    # Create an ordered dictionary for the results, mapping states to apportioned
    # congressional seats, and start each state with one seat. We use an ordered
    # dictionary to keep track of the last state to get a seat.
    results = collections.OrderedDict(**{k: 1 for k in census_data.keys()})

    # Since we start each state with one seat, subtract those from the total
    num_seats -= len(census_data)

    # Keep iterating over the states, allocating seats, until no seats remain.
    while num_seats > 0:
        highest_a = 0
        highest_state = None
        for state, population in census_data.items():
            n = results[state] + 1
            a = population / sqrt(n * (n - 1))
            if a > highest_a:
                highest_a = a
                highest_state = state
                results.move_to_end(state)
        results[highest_state] += 1
        num_seats -= 1

    return results
