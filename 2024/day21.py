import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
from utils import *


num_pad = {
    Point(0,0): '7',
    Point(1,0): '8',
    Point(2,0): '9',
    Point(0,1): '4',
    Point(1,1): '5',
    Point(2,1): '6',
    Point(0,2): '1',
    Point(1,2): '2',
    Point(2,2): '3',
    Point(0,3): '',
    Point(1,3): '0',
    Point(2,3): 'A',
}
num_pad = {value: key for key, value in num_pad.items()}


robot = {
    Point(0, 3): '',
    Point(1, 3): '^',
    Point(2, 3): 'A',
    Point(0, 4): '<',
    Point(1, 4): 'v',
    Point(2, 4): '>',
}
robot = {value: key for key, value in robot.items()}

moves = {
    '<': Offset.LEFT,
    '>': Offset.RIGHT,
    '^': Offset.UP,
    'v': Offset.DOWN
}
# moves = {value: key for key, value in moves.items()}

@functools.cache
def get_path(start: Point, end: Point):
    q = collections.deque([(start, 0, (start,), "")])

    while q:
        location, distance, path, buttons = q.popleft()

        if location == end:
            return buttons

        if distance > 10:
            continue

        for char, offset in moves.items():
            neighbor = location + offset
            if neighbor not in path:
                q.append((neighbor, distance + 1, path + neighbor, buttons + char))


def press_buttons(buttons, start=Point(2, 3)):
    arm_position = start
    movements = []

    for button in buttons:
        if button in num_pad:
            goal = num_pad[button]
        else:
            goal = robot[button]

        movement = get_path(arm_position, goal)

        arm_position = goal

        movements.append(movement + 'A')

    return ''.join(movements)




def part1(data):
    codes = [code.rstrip() for code in data]

    acc = 0

    for code in codes:
        buttons = press_buttons(code)
        buttons = press_buttons(buttons)
        buttons = press_buttons(buttons)
        # buttons = press_buttons(buttons)

        print(f'code {code}:\t {len(buttons) * extract_ints(code)[0]}\t = {len(buttons)} * {extract_ints(code)[0]}')
        acc += len(buttons) * extract_ints(code)[0]

    return acc


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
