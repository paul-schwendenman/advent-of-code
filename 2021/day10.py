import fileinput
from functools import reduce

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

autocomplete_points = {
    '(':1,
    '[':2,
    '{':3,
    '<':4
}

def part1(lines):
    stack = []
    corrupted = []
    for line in lines:
        illegal = None
        for char in line:
            if char in '({[<':
                stack.append(char)
            elif char == ')':
                pair = stack.pop()

                if pair != '(':
                    illegal = char
                    break
            elif char == '}':
                pair = stack.pop()

                if pair != '{':
                    illegal = char
                    break
            elif char == ']':
                pair = stack.pop()

                if pair != '[':
                    illegal = char
                    break
            elif char == '>':
                pair = stack.pop()

                if pair != '<':
                    illegal = char
                    break
        if illegal:
            corrupted.append(illegal)

    # print(corrupted)

    return sum(points[item] for item in corrupted)

def part2(lines):
    missing = []
    corrupted = []
    for line in lines:
        stack = []
        illegal = None
        for char in line:
            if char in '({[<':
                stack.append(char)
            elif char == ')':
                pair = stack.pop()

                if pair != '(':
                    illegal = char
                    break
            elif char == '}':
                pair = stack.pop()

                if pair != '{':
                    illegal = char
                    break
            elif char == ']':
                pair = stack.pop()

                if pair != '[':
                    illegal = char
                    break
            elif char == '>':
                pair = stack.pop()

                if pair != '<':
                    illegal = char
                    break
        if not illegal and stack:
            missing.append(stack)
            # corrupted.append(illegal)

    # print(["".join(group) for group in missing])

    # print(reduce(lambda a, b: a * 5 + autocomplete_points[b], '[])}>', 0))
    scores = list(sorted(reduce(lambda a, b: a * 5 + autocomplete_points[b], reversed(group), 0) for group in missing))
    # print(scores)
    return scores[len(scores)//2]


def main():
    with fileinput.input() as input:
        lines = [line.rstrip() for line in input]

    print(part1(lines))
    print(part2(lines))

if __name__ == '__main__':
    main()