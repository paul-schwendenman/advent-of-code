import fileinput
from dataclasses import dataclass
from typing import Tuple


def parse(string):
    return eval(string)


def reduce(number):
    pass

def expode(number):
    pass


def split(number: int) -> Tuple[bool, list]:
    if isinstance(number, int):
        if number > 9:
            return True, [number // 2, (number+1) // 2]
        else:
            return False, number

    [x, y] = number

    changed, new_x = split(x)

    if changed:
        return changed, [new_x, y]

    changed, new_y = split(y)

    if changed:
        return changed, [x, new_y]

    return False, number


def add(number_1, number_2):
    return [number_1, number_2]


def magnitude(number):
    if isinstance(number, int):
        return number

    [x, y] = number

    return 3 * magnitude(x) + 2 * magnitude(y)


def part1(data):

    numbers = [parse(item) for item in data]
    pass


def part2(data):
    pass


def main():
    with fileinput.input() as input:
        data = [line.rstrip() for line in input]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
