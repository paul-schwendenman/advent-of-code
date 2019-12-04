map_parens = {
    '(': 1,
    ')': -1,
}


def count_parens(instructions):
    return sum(map_parens[instruction] for instruction in instructions)


def main():
    pass


if __name__ == "__main__":
    main()
