import fileinput
from enum import Enum


class Instruction(Enum):
    FORWARD = "forward"
    UP = "up"
    DOWN = "down"


def parse_command(command):
    [instruction, value] = command.split(" ")

    return Instruction(instruction), int(value)


def part1(commands):
    x, y = 0, 0

    for command in commands:
        instruction, distance = parse_command(command)

        if instruction == Instruction.FORWARD:
            x += distance
        elif instruction == Instruction.UP:
            y -= distance
        elif instruction == Instruction.DOWN:
            y += distance
        else:
            raise ValueError(command)

    return x * y


def part2(commands):
    x, y, aim = 0, 0, 0

    for command in commands:
        instruction, value = parse_command(command)

        if instruction == Instruction.FORWARD:
            x += value
            y += value * aim
        elif instruction == Instruction.UP:
            aim -= value
        elif instruction == Instruction.DOWN:
            aim += value
        else:
            raise ValueError(command)

    return x * y


def main():
    with fileinput.input() as lines:
        lines = list(lines)

    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
