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


def part1(data: List[str], target: str = 'shiny gold') -> int:
    commands = parse_program(data)
    acc = 0
    cur = 0

    pos = []

    while cur not in pos:
        pos.append(cur)
        instruction, value = commands[cur]

        if instruction == 'nop':
            cur += 1
        elif instruction == 'jmp':
            cur += value
        elif instruction == 'acc':
            acc += value
            cur += 1

    return acc


def runner(commands: Program) -> Optional[int]:
    acc = 0
    cur = 0

    pos = []

    try:
        while cur not in pos:
            pos.append(cur)
            instruction, value = commands[cur]

            if instruction == 'nop':
                cur += 1
            elif instruction == 'jmp':
                cur += value
            elif instruction == 'acc':
                acc += value
                cur += 1
    except IndexError:
        return acc
    else:
        return None


def part2(data: List[str]) -> int:
    commands = parse_program(data)

    programs = []

    for cur, command in enumerate(commands):
        instruction, value = command
        if instruction == "nop":
            new_prog = commands.copy()
            new_prog[cur] = ('jmp', value)
            programs.append(new_prog)
        elif instruction == 'jmp':
            new_prog = commands.copy()
            new_prog[cur] = ('nop', value)
            programs.append(new_prog)

    return [value for value in (runner(program) for program in programs) if value is not None][0]




def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
