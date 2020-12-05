from contextlib import contextmanager
from typing import List
import fileinput


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line.rstrip() for line in data]


def find_seat_id(boarding_pass: str) -> int:
    seat = boarding_pass.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')

    return int(seat, base=2)


def part1(data: List[str]) -> int:
    return max([find_seat_id(boarding_pass) for boarding_pass in data])


def part2(data: List[str]) -> int:
    passes = ([find_seat_id(boarding_pass) for boarding_pass in data])

    for seat_id in range(min(passes), max(passes)):
        if seat_id not in passes:
            return seat_id
    else:
        raise ValueError("No missing seats")


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
