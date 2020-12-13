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


def find_schedule_timestamp(raw_schedule: str) -> int:
    return 1068781


def part2(data: List[str]) -> int:
    return find_schedule_timestamp(data[1])


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
