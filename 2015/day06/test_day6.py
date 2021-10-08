import pytest
from day6 import part1


@pytest.mark.parametrize("commands,expected_count", [
  (["turn on 0,0 through 999,999"], 1_000_000),
  (["toggle 0,0 through 999,0"], 1_000),
  (["turn on 0,0 through 999,999", "turn off 499,499 through 500,500"], 1_000_000 - 4),
])
def test_is_nice_string(commands, expected_count):
    assert expected_count == part1(commands)