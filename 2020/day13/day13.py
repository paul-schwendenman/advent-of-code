from __future__ import annotations
from typing import List
from aoc import readfile


def part1(data: List[str]) -> int:
    '''
    >>> a = lambda b,c: (((b//c)+1)*c) - b
    >>> a(1004345,41)
    32
    >>> a(1004345,37)
    20
    >>> [a(1004345,x) for x in (41,37,379,23,13,17, 29,557,19)]
    [32, 20, 5, 19, 9, 15, 12, 483, 14]
    >>> [x, a(1004345,x) for x in (41,37,379,23,13,17, 29,557,19)]
    File "<stdin>", line 1
        [x, a(1004345,x) for x in (41,37,379,23,13,17, 29,557,19)]
                        ^
    SyntaxError: invalid syntax
    >>> [(x, a(1004345,x)) for x in (41,37,379,23,13,17, 29,557,19)]
    [(41, 32), (37, 20), (379, 5), (23, 19), (13, 9), (17, 15), (29, 12), (557, 483), (19, 14)]
    >>> 379*5
    '''
    pass

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
        print(part2(data))


if __name__ == '__main__':
    main()
