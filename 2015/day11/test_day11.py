import pytest
from day11 import next_password, has_two_pairs, has_confusing_letters, has_straight, is_valid, next_valid_password


@pytest.mark.parametrize("input,expected", [("xx", "xy"), ("xy", "xz",), ("xz", "ya"), ("ya", "yb")])
def test_next_password(input, expected):
    assert expected == next_password(input)


@pytest.mark.parametrize("input,expected", [("cqjxynyu", "cqjxynyv"), ("cqjxynza", "cqjxynzb",)])
def test_next_password_more(input, expected):
    assert expected == next_password(input)


@pytest.mark.parametrize("input,expected", [("hijklmmn", False), ("abbceffg", True), ("abbcegjk", False), ("abcdffaa", True), ("ghjaabcc", True)])
def test_has_two_pairs(input, expected):
    assert expected == has_two_pairs(input)


@pytest.mark.parametrize("input,expected", [("hijklmmn", True), ("abbceffg", False), ("abbcegjk", False), ("abcdffaa", False), ("ghjaabcc", False)])
def test_has_confusing_letters(input, expected):
    assert expected == has_confusing_letters(input)

@pytest.mark.parametrize("input,expected", [("hijklmmn", True), ("abbceffg", False), ("abbcegjk", False), ("abcdffaa", True), ("ghjaabcc", True)])
def test_has_straight(input, expected):
    assert expected == has_straight(input)

@pytest.mark.parametrize("input,expected", [("hijklmmn", False), ("abbceffg", False), ("abbcegjk", False), ("abcdffaa", True), ("ghjaabcc", True)])
def test_is_valid(input, expected):
    assert expected == is_valid(input)

def test_is_valid2():
    assert is_valid("cqkaabcc")

# @pytest.mark.parametrize("input,expected", [("abcdefgh", "abcdffaa"), ("ghijklmn", "ghjaabcc")])
# def test_next_valid_password(input, expected):
#     assert expected == next_valid_password(input)