"""

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
    results = collections.OrderedDict(**{k: 1 for k in census_data.keys()})
    num_seats -= len(census_data)

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
