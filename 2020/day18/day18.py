from __future__ import annotations
from typing import DefaultDict, Iterator, Sequence
from aoc import readfile
from collections import defaultdict, namedtuple


def parse_math(line: str):
    print(f'\nline: {line}')
    if line[0] == '(':
        parens = 0
        for index, char in enumerate(line):
            if char == '(':
                parens += 1
            elif char == ')':
                parens -= 1
            if parens == 0:
                break
        # print(f'front: "{line[1:index]}"')
        print(f'back: "{line[index+1:]}"')
        print(f'parse_math(parse_math({line[1:index]}){line[index+1:]})')
        return parse_math(f'{parse_math(line[1:index])}{line[index+1:]}')
    parts = line.split(' ', 2)

    if len(parts) == 1:
        print(f'"{parts[0]}"')
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
        # print(f'front: "{line[1:index]}"')
        print(f'''parse_math(parse_math({left} {opp} {f'parse_math({rest[1:index]})'}){rest[index+1:]})''')
        return parse_math(f"{parse_math(f'{left} {opp} {parse_math(rest[1:index])}')}{rest[index+1:]}")

    rest_parts = rest.split(' ', 1)
    if len(rest_parts) == 1:
        if opp == '*':
            print(f'{int(left) * int(rest_parts[0])}')
            return f'{int(left) * int(rest_parts[0])}'
        elif opp == '+':
            print(f'{int(left) + int(rest_parts[0])}')
            return f'{int(left) + int(rest_parts[0])}'
    else:
        if opp == '*':
            print(f"parse_math({int(left) * int(rest_parts[0])} {rest_parts[1]})")
            return parse_math(f'{int(left) * int(rest_parts[0])} {rest_parts[1]}')
        elif opp == '+':
            print(f"parse_math({int(left) + int(rest_parts[0])} {rest_parts[1]})")
            return parse_math(f'{int(left) + int(rest_parts[0])} {rest_parts[1]}')

    pass


    # print(line)
    # if line[0] == '(':
    #     parens = 1
    #     for index, char in enumerate(line[1:]):
    #         if char == '(':
    #             parens += 1
    #         else char == ')':
    #             parens -= 1
    #         if parens == 0:
    #             parse_math(1:index)

def part1(data: Sequence[str]) -> int:
    answers = []
    for line in data:
        answer = parse_math(line)
        print(f'{line} = {answer}')
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
