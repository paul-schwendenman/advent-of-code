def calculate_houses(path):
    houses = set()
    position = (0, 0)

    houses.add(position)

    for location in path:
        if location == '>':
            x, y = position
            position = x + 1, y
            houses.add(position)
        elif location == '<':
            x, y = position
            position = x - 1, y
            houses.add(position)
        elif location == '^':
            x, y = position
            position = x, y + 1
            houses.add(position)
        elif location == 'v':
            x, y = position
            position = x, y - 1
            houses.add(position)

    return houses


def main():
    with open("day03/input") as input_file:
        path = input_file.readlines()[0]

    houses = len(calculate_houses(path))
    print(houses)


if __name__ == "__main__":
    main()
