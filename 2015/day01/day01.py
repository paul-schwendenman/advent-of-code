map_parens = {
    '(': 1,
    ')': -1,
    '\n': 0,
}


def count_parens(instructions):
    return sum(map_parens[instruction] for instruction in instructions)


def find_basement(instructions):
    floor = 0
    for counter, instruction in enumerate(instructions):
        floor += map_parens[instruction]
        if floor < 0:
            break

    return counter + 1


def main():
    with open("day01/input") as input_file:
        instructions = input_file.readlines()[0]

    print(count_parens(instructions))
    print(find_basement(instructions))


if __name__ == "__main__":
    main()
