from __future__ import annotations
from typing import List
from aoc import readfile


def calculate_time_until_bus(bus_id: int, timestamp: int) -> int:
    return bus_id - (timestamp % bus_id)


def part1(data: List[str]) -> int:
    timestamp = int(data[0])
    bus_ids = [int(bus) for bus in data[1].split(',') if bus != 'x']

    arrival_times = sorted(
        ((bus_id, calculate_time_until_bus(bus_id, timestamp)) for bus_id in bus_ids),
        key=lambda item: item[1]
    )

    next_bus, wait = arrival_times[0]

    return next_bus * wait


def check(buses, t):
    for index, bus in enumerate(buses):
        if bus == 'x':
            continue
        bus_id = int(bus)

        if ((t+index) % bus_id) != 0:
            # print(bus_id, t, t+index)
            return True
    else:
        return False


def part2(data: List[str]) -> int:
    '''
    >>> buses = "41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,379,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,557,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19".split(',')
    >>> buses = [(index, int(bus_id)) for index, bus_id in enumerate(buses) if bus_id != 'x']
    >>> buses
    [(0, 41), (35, 37), (41, 379), (49, 23), (54, 13), (58, 17), (70, 29), (72, 557), (91, 19)]
    '''
    # buses = "17,x,13,19".split(',')
    # buses = "7,13,x,x,59,x,31,19".split(',')
    buses = "41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,379,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,557,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19".split(',')
    pass

    t = 0
    n = 0
    while check(buses, t):
        # print(t)
        t += int(buses[0])


    print("match", t)


def main() -> None:
    with readfile() as data:
        print(part1(data))
        # print(part2(data))


if __name__ == '__main__':
    main()
