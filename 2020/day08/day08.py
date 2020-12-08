from contextlib import contextmanager
from typing import List, Optional, Tuple
import fileinput


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line.rstrip() for line in data]


Command = Tuple[str, int]
Program = List[Command]


def parse_command(command: str) -> Command:
    instruction, value = command.split(' ')

    return instruction, int(value)


def parse_program(commands: List[str]) -> Program:
    return [parse_command(command) for command in commands]


def run_progam(program: Program, acc: int = 0, cursor: int = 0) -> Tuple[int, int]:
    previous_cursors = []

    while (cursor not in previous_cursors) and (cursor < len(program)):
        previous_cursors.append(cursor)

        instruction, value = program[cursor]

        if instruction == 'nop':
            cursor += 1
        elif instruction == 'jmp':
            cursor += value
        elif instruction == 'acc':
            acc += value
            cursor += 1

    return cursor, acc


def part1(data: List[str]) -> int:
    commands = parse_program(data)

    cur, acc = run_progam(commands)

    return acc


def part2(data: List[str]) -> int:
    commands = parse_program(data)
    goal = len(commands)
    programs = []

    for index, command in enumerate(commands):
        instruction, value = command
        if instruction == "nop":
            new_prog = commands.copy()
            new_prog[index] = ('jmp', value)
            programs.append(new_prog)
        elif instruction == 'jmp':
            new_prog = commands.copy()
            new_prog[index] = ('nop', value)
            programs.append(new_prog)

    for program in programs:
        cursor, acc = run_progam(program)

        if cursor == goal:
            break

    return acc


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
