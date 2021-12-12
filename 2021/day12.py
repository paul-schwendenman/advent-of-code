import fileinput
from collections import defaultdict


def traverse(caves, start, goal):
    paths = []

    def inner(innerstart, path=[start]):
        for next in caves[innerstart]:
            if next == goal:
                paths.append(path + [next])
            elif next.islower() and next in path:
                continue
            else:
                inner(next, path + [next])

    inner(start)

    return paths


def part1(lines):
    pairs = [line.split("-") for line in lines]

    paths = defaultdict(list)

    for start, end in pairs:
        paths[start].append(end)
        paths[end].append(start)

    solutions = traverse(paths, "start", "end")

    return len(solutions)


def traverse2(caves, start, goal):
    paths = []

    def inner(innerstart, path=[start], twice=False, depth=1):
        for next in caves[innerstart]:
            if next == goal:
                paths.append(path + [next])
            elif next.islower() and next in path:
                if not twice and next not in (start, goal):
                    inner(next, path + [next], True, depth=depth + 1)
                continue
            else:
                inner(next, path + [next], twice, depth=depth + 1)

    inner(start)

    return paths


def part2(lines):
    pairs = [line.split("-") for line in lines]

    paths = defaultdict(list)

    for start, end in pairs:
        paths[start].append(end)
        paths[end].append(start)

    solutions = traverse2(paths, "start", "end")

    return len(solutions)


def main():
    with fileinput.input() as input:
        lines = [line.rstrip() for line in input]

    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
