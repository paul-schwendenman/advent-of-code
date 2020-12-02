from collections import Counter
from dataclasses import dataclass
import fileinput
import re


@dataclass
class Password():
    lower_bound: int
    upper_bound: int
    target_char: str
    password: str

    _pattern = re.compile(r'(?P<lower_bound>[0-9]+)-(?P<upper_bound>[0-9]+) (?P<target_char>.): (?P<password>.+)')

    def __init__(self, lower_bound, upper_bound, target_char, password):
        self.lower_bound = int(lower_bound)
        self.upper_bound = int(upper_bound)
        self.target_char = target_char
        self.password = password

    @classmethod
    def make(cls, line):
        match = cls._pattern.match(line).groupdict()

        return cls(**match)

    @property
    def lower_char(self):
        return self.password[self.lower_bound - 1]

    @property
    def upper_char(self):
        return self.password[self.upper_bound - 1]

    def counts(self):
        return Counter(self.password)


def is_valid_part1_password(line):
    password = Password.make(line)
    count = password.counts()[password.target_char]

    return password.lower_bound <= count and count <= password.upper_bound


def is_valid_part2_password(line):
    password = Password.make(line)

    lower_match = password.lower_char == password.target_char
    upper_match = password.upper_char == password.target_char

    return lower_match ^ upper_match


def part1(lines):
    return sum([is_valid_part1_password(line) for line in lines])


def part2(lines):
    return sum([is_valid_part2_password(line) for line in lines])


def main():
    with fileinput.input() as data:
        lines = list(data)

    print(part1(lines))
    print(part2(lines))


if __name__ == '__main__':
    main()
