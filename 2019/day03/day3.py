def manhattan_distance(pos_a, pos_b):
    return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])


def spilt_instruction(instruction):
    return instruction[0], int(instruction[1:])


def convert_instructions_to_path(instructions):
    x, y = 0, 0
    path = []

    for instruction in instructions:
        direction, length = spilt_instruction(instruction)
        if direction == 'R':
            for i in range(length):
                x += 1
                path.append((x, y))
        elif direction == 'L':
            for i in range(length):
                x -= 1
                path.append((x, y))
        elif direction == 'U':
            for i in range(length):
                y += 1
                path.append((x, y))
        elif direction == 'D':
            for i in range(length):
                y -= 1
                path.append((x, y))
    return path


def find_intersections(path1, path2):
    return set(path1).intersection(set(path2))


def find_closest_intersection(coords):
    return min(manhattan_distance((0, 0), coord) for coord in coords)


def find_signal_delay(coords, path1, path2):
    return min(path1.index(coord) + path2.index(coord) + 2 for coord in coords)


def main(path1, path2):
    path1 = convert_instructions_to_path(path1.split(','))
    path2 = convert_instructions_to_path(path2.split(','))

    coords = find_intersections(path1, path2)

    return find_closest_intersection(coords)


def main2(path1, path2):
    path1 = convert_instructions_to_path(path1.split(','))
    path2 = convert_instructions_to_path(path2.split(','))

    coords = find_intersections(path1, path2)

    return find_signal_delay(coords, path1, path2)


if __name__ == "__main__":
    with open('input') as input:
        lines = input.readlines()

    print(main2(lines[0], lines[1]))
