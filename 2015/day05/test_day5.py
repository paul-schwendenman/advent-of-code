import pytest

from day5 import has_restricted_pairs, has_double_letter, has_three_vowels, is_nice_string, is_nice_string2

def test_has_three_vowels():
    assert has_three_vowels("aei") is True


def test_has_double_letter():
    assert has_double_letter("aa") is True


@pytest.mark.parametrize("word", ["ab", "cd", "pq", "xy"])
def test_has_restricted_pairs(word):
    assert has_restricted_pairs(word)


@pytest.mark.parametrize("word", ["aa", "ddd"])
def test_not_has_restricted_pairs(word):
    assert not has_restricted_pairs(word)


@pytest.mark.parametrize("word,expected", [("ugknbfddgicrmopn", True), ("aaa", True), ("jchzalrnumimnmhp", False), ("haegwjzuvuyypxyu", False), ("dvszwmarrgswjxmb", False)])
def test_is_nice_string(word, expected):
    assert expected is is_nice_string(word)


@pytest.mark.parametrize("word,expected", [("qjhvhtzxzqqjkmpb", True), ("xxyxx", True), ("uurcxstgmygtbstg", False), ("ieodomkazucvgmuy", False)])
def test_is_nice_string2(word, expected):
    assert expected is is_nice_string2(word)
