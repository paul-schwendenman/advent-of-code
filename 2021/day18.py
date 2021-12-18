import fileinput
from dataclasses import dataclass
from typing import Tuple
from functools import reduce
from itertools import combinations


def parse(string):
    return eval(string)


def reducer(number):
    while True:
        changed, number, _, _ = explode(number)

        if changed:
            continue

        changed, number = split(number)

        if not changed:
            break

    return number


def to_right(base, new):
    if isinstance(base, int):
        return base + new

    x, y = base

    return [x, to_right(y, new)]


def to_left(base, new):
    if isinstance(base, int):
        return base + new

    x, y = base

    return [to_left(x, new), y]


def explode(number, depth=0) -> Tuple[bool, int, int, int]:
    if isinstance(number, int):
        return False, number, 0, 0

    x, y = number

    if depth >= 4:
        return True, 0, x, y

    changed, next, left, right = explode(x, depth + 1)

    if changed:
        number = [next, to_left(y, right)]
        return True, number, left, 0

    changed, next, left, right = explode(y, depth + 1)

    if changed:
        number = [to_right(x, left), next]

        return True, number, 0, right

    return False, number, 0, 0


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
    return reducer([number_1, number_2])


def magnitude(number):
    if isinstance(number, int):
        return number

    [x, y] = number

    return 3 * magnitude(x) + 2 * magnitude(y)


def part1(data):

    numbers = [parse(item) for item in data]

    result = reduce(add, numbers)

    return magnitude(result)


def part2(data):
    numbers = [parse(item) for item in data]

    return max(magnitude(add(num1, num2)) for num1,  num2 in combinations(numbers, 2))


def main():
    with fileinput.input() as input:
        data = [line.rstrip() for line in input]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
