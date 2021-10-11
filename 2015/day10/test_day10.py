import pytest
from day10 import look_and_say


@pytest.mark.parametrize("input,expected", [("1", "11"), ("11", "21"), ("21", "1211"), ("1211", "111221"), ("111221", "312211")])
def test_look_and_see(input, expected):
    assert expected == look_and_say(input)