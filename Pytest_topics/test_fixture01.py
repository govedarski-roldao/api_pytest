import pytest


@pytest.fixture()
def setup_list():
    print("\n in fixtures.. \n")
    city = ["New York", "London", "Paris", "Los Angeles", "Mumbai"]
    return city


def test_getItem01(setup_list):
    city = setup_list
    print(setup_list[1:3])
    assert city[0] == 'New York'
    assert setup_list[::2] == ["New York", "Paris", "Mumbai"]

def test_reverse01(setup_list):
    assert setup_list[::-2] == ["Mumbai", "Paris", "New York"]
