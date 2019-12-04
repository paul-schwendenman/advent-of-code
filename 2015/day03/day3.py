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

    santa_path = (house for counter, house in enumerate(path) if counter % 2 == 0)
    robot_path = (house for counter, house in enumerate(path) if counter % 2 == 1)

    santa_houses = calculate_houses(santa_path)
    robot_houses = calculate_houses(robot_path)
    print(len(santa_houses.union(robot_houses)))


if __name__ == "__main__":
    main()
