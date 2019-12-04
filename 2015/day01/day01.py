map_parens = {
    '(': 1,
    ')': -1,
    '\n': 0,
}


def count_parens(instructions):
    return sum(map_parens[instruction] for instruction in instructions)


def main():
    with open("day01/input") as input_file:
        instructions = input_file.readlines()[0]

    print(count_parens(instructions))


if __name__ == "__main__":
    main()
