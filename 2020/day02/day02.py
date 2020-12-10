from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import List, ClassVar
import fileinput
import re


@dataclass
class Password():
    lower_bound: int
    upper_bound: int
    target_char: str
    password: str

    _pattern: ClassVar[re.Pattern] = re.compile(r'(?P<lower_bound>[0-9]+)-(?P<upper_bound>[0-9]+) (?P<target_char>.): (?P<password>.+)')

    def __init__(self, lower_bound, upper_bound, target_char, password):
        self.lower_bound = int(lower_bound)
        self.upper_bound = int(upper_bound)
        self.target_char = target_char
        self.password = password

    @classmethod
    def make(cls, line: str) -> Password:
        match = cls._pattern.match(line)

        if match:
            return cls(**match.groupdict())

        raise ValueError("Invalid Password")

    @property
    def lower_char(self):
        return self.password[self.lower_bound - 1]

    @property
    def upper_char(self):
        return self.password[self.upper_bound - 1]

    def counts(self) -> Counter:
        return Counter(self.password)


def sled_rental_rule(line: str) -> bool:
    password = Password.make(line)
    count = password.counts()[password.target_char]

    return bool(password.lower_bound <= count <= password.upper_bound)


def official_toboggan_rule(line: str) -> bool:
    password = Password.make(line)

    lower_match = password.lower_char == password.target_char
    upper_match = password.upper_char == password.target_char

    return bool(lower_match ^ upper_match)


def part1(lines: List[str]) -> int:
    return sum([sled_rental_rule(line) for line in lines])


def part2(lines: List[str]) -> int:
    return sum([official_toboggan_rule(line) for line in lines])


def main() -> None:
    with fileinput.input() as data:
        lines = list(data)

    print(part1(lines))
    print(part2(lines))


if __name__ == '__main__':
    main()
