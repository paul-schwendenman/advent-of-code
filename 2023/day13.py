import fileinput


def transpose(grid):
    return list(zip(*grid))


def extract_patterns(data):
    lines = ''.join(data)

    for chunk in lines.split('\n\n'):
        yield chunk.strip().split('\n')


def count_diff(a, b):
    return sum(1 for i, j in zip(a, b) if i != j)


def find_horizontal_reflection(pattern, smudges=0):
    for index, _ in enumerate(pattern[1:], start=1):
        before = reversed(pattern[:index])
        after = pattern[index:]

        if sum(count_diff(*pair) for pair in zip(before, after)) == smudges:
            return index

    return 0


def find_vertical_reflection(pattern, smudges=0):
    return find_horizontal_reflection(transpose(pattern), smudges)


def find_reflection(pattern, smudges=0):
    horizontal = find_horizontal_reflection(pattern, smudges)
    vertical = find_vertical_reflection(pattern, smudges)

    return horizontal * 100 + vertical


def part1(data):
    patterns = list(extract_patterns(data))

    return sum(find_reflection(pattern, 0) for pattern in patterns)


def part2(data):
    patterns = list(extract_patterns(data))

    return sum(find_reflection(pattern, 1) for pattern in patterns)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
