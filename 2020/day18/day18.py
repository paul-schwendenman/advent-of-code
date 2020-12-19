from __future__ import annotations
from typing import Sequence
from aoc import readfile


def parse_math(line: str) -> str:
    if line[0] == '(':
        parens = 0
        for index, char in enumerate(line):
            if char == '(':
                parens += 1
            elif char == ')':
                parens -= 1
            if parens == 0:
                break
        return parse_math(f'{parse_math(line[1:index])}{line[index+1:]}')
    parts = line.split(' ', 2)

    if len(parts) == 1:
        return parts[0]
    left, opp, rest = parts

    if rest[0] == '(':
        parens = 0
        for index, char in enumerate(rest):
            if char == '(':
                parens += 1
            elif char == ')':
                parens -= 1
            if parens == 0:
                break
        return parse_math(f"{parse_math(f'{left} {opp} {parse_math(rest[1:index])}')}{rest[index+1:]}")

    rest_parts = rest.split(' ', 1)
    if len(rest_parts) == 1:
        if opp == '*':
            return f'{int(left) * int(rest_parts[0])}'
        elif opp == '+':
            return f'{int(left) + int(rest_parts[0])}'
    else:
        if opp == '*':
            return parse_math(f'{int(left) * int(rest_parts[0])} {rest_parts[1]}')
        elif opp == '+':
            return parse_math(f'{int(left) + int(rest_parts[0])} {rest_parts[1]}')
        else:
            raise ValueError(f'Invalid operator {opp}')


def part1(data: Sequence[str]) -> int:
    answers = []
    for line in data:
        answer = parse_math(line)
        answers.append(int(answer))

    return sum(answers)


def part2(data: Sequence[str]) -> int:
    pass


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
