"""
Unit tests for testing the Huntington–Hill method of equal proportions.

These tests compare the congressional seat allocations that we calculate
with the actual (and fake) numbers, using real (and fake) census data.
"""

from huntington_hill import __version__, calculate_apportionment


# The test data below are maps of state abbreviations to a tuple of population
# and (correct) number of congressional seats, which is used to compare the
# results of the calculation function with the actual value.

# The official 2010 census population data, and the official resulting number of
# congressional seats for each state.
TEST_DATA_2010 = {
    "CA": (37253956, 53),
    "TX": (25145561, 36),
    "FL": (18801310, 27),
    "NY": (19378102, 27),
    "IL": (12830632, 18),
    "PA": (12702379, 18),
    "OH": (11536504, 16),
    "GA": (9687653, 14),
    "NC": (9535483, 13),
    "MI": (9883640, 14),
    "NJ": (8791894, 12),
    "VA": (8001024, 11),
    "WA": (6724540, 10),
    "AZ": (6392017, 9),
    "IN": (6483802, 9),
    "MA": (6547629, 9),
    "TN": (6346105, 9),
    "CO": (5029196, 7),
    "MD": (5773552, 8),
    "MN": (5303925, 8),
    "MO": (5988927, 8),
    "WI": (5686986, 8),
    "AL": (4779736, 7),
    "SC": (4625364, 7),
    "KY": (4339367, 6),
    "LA": (4533372, 6),
    "OR": (3831074, 5),
    "CT": (3574097, 5),
    "OK": (3751351, 5),
    "AR": (2915918, 4),
    "IA": (3046355, 4),
    "KS": (2853118, 4),
    "MS": (2967297, 4),
    "NV": (2700551, 4),
    "UT": (2763885, 4),
    "NE": (1826341, 3),
    "NM": (2059179, 3),
    "HI": (1360301, 2),
    "ID": (1567582, 2),
    "ME": (1328361, 2),
    "MT": (989415, 1),
    "NH": (1316470, 2),
    "RI": (1052567, 2),
    "WV": (1852994, 3),
    "AK": (710231, 1),
    "DE": (897934, 1),
    "ND": (672591, 1),
    "SD": (814180, 1),
    "VT": (625741, 1),
    "WY": (563626, 1),
}
# The total number of congressional seats in 2010 (fixed at 435 since 1930)
SEAT_COUNT_2010 = 435

# The official 2020 census population data, and the official resulting number of
# congressional seats for each state.
TEST_DATA_2020 = {
    "CA": (39538223, 52),
    "TX": (29145505, 38),
    "FL": (21538187, 28),
    "NY": (20201249, 26),
    "PA": (13002700, 17),
    "IL": (12812508, 17),
    "OH": (11799448, 15),
    "GA": (10711908, 14),
    "NC": (10439388, 14),
    "MI": (10077331, 13),
    "NJ": (9288994, 12),
    "VA": (8631393, 11),
    "WA": (7705281, 10),
    "AZ": (7151502, 9),
    "MA": (7029917, 9),
    "TN": (6910840, 9),
    "IN": (6785528, 9),
    "MD": (6177224, 8),
    "MO": (6154913, 8),
    "WI": (5893718, 8),
    "CO": (5773714, 8),
    "MN": (5706494, 8),
    "SC": (5118425, 7),
    "AL": (5024279, 7),
    "LA": (4657757, 6),
    "KY": (4505836, 6),
    "OR": (4237256, 6),
    "OK": (3959353, 5),
    "CT": (3605944, 5),
    "UT": (3271616, 4),
    "IA": (3190369, 4),
    "NV": (3104614, 4),
    "AR": (3011524, 4),
    "MS": (2961279, 4),
    "KS": (2937880, 4),
    "NM": (2117522, 3),
    "NE": (1961504, 3),
    "ID": (1839106, 2),
    "WV": (1793716, 2),
    "HI": (1455271, 2),
    "NH": (1377529, 2),
    "ME": (1362359, 2),
    "RI": (1097379, 2),
    "MT": (1084225, 2),
    "DE": (989948, 1),
    "SD": (886667, 1),
    "ND": (779094, 1),
    "AK": (733391, 1),
    "VT": (643077, 1),
    "WY": (576851, 1),
}
# The total number of congressional seats in 2020 (fixed at 435 since 1930)
SEAT_COUNT_2020 = 435

# The fake example census data used to explain how calculations work on
# the US census web site
TEST_DATA_FAKE = {}
SEAT_COUNT_FAKE = 0


def test_version():
    """A goofy test that `poetry init` writes."""
    assert __version__ == "0.1.0"


def do_data_test(test_data, seat_count):
    """
    Try the allocation function using a map of states to populations and compare with the
    correct seat allocations.

    :param test_data: A map of state to a tuple of population and seats, to be used as test data
    :param seat_count: The total number of seats to allocate
    """
    # Create a map of states to populations
    test_input = {k: v[0] for k, v in test_data.items()}
    # Run the allocation function and collect the output
    test_output = calculate_apportionment(test_input, seat_count)
    # The number of states in the input should be the same as the number of states in the output
    assert len(test_data) == len(test_output)
    # The sum of the seats in the output should equal the total number of seats
    assert seat_count == sum(test_output.values())
    # Compare the number of seats in each state in the output to the test data expectation
    for state, seats in test_output.items():
        assert test_data[state][1] == seats


def test_2010_data():
    """Test the official 2010 census data."""
    do_data_test(TEST_DATA_2010, SEAT_COUNT_2010)


def test_2020_data():
    """Test the official 2020 census data."""
    do_data_test(TEST_DATA_2020, SEAT_COUNT_2020)


def test_FAKE_data():
    """Test the fake census data use in examples on the US census bureau web site"""
    do_data_test(TEST_DATA_FAKE, SEAT_COUNT_FAKE)
