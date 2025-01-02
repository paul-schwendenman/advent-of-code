import fileinput

def walk_path(instructions):
    facing = {
        1: "N",
        -1: "S",
        (-1j): "W",
        (1j): "E",
    }
    x, y, f = 0, 0, 1

    for instruction in instructions:
        instruction = instruction.strip()
        turn, length = instruction[0], int(instruction[1:])

        if turn == 'L':
            f *= -1j
        elif turn == 'R':
            f *= 1j
        else:
            raise ValueError(instruction)

        if f == 1:
            x += length
        elif f == -1:
            x -= length
        elif f == 1j:
            y += length
        elif f == -1j:
            y -= length
        else:
            ValueError(f'facing: {f}')

    print(f'{x=}, {y=}, {f=}, {facing[f]}')
    return abs(x) + abs(y)


def walk_path2(instructions):
    facing = {
        1: "N",
        -1: "S",
        (-1j): "W",
        (1j): "E",
    }
    x, y, f = 0, 0, 1

    seen = set()

    for instruction in instructions:
        instruction = instruction.strip()
        turn, length = instruction[0], int(instruction[1:])

        if turn == 'L':
            f *= -1j
        elif turn == 'R':
            f *= 1j
        else:
            raise ValueError(instruction)

        for i in range(length):
            if f == 1:
                x += 1 #length
            elif f == -1:
                x -= 1 #length
            elif f == 1j:
                y += 1 #length
            elif f == -1j:
                y -= 1 #length
            else:
                ValueError(f'facing: {f}')

            # if (x, y) in seen:
            #     break
            seen.add((x, y))

    print(f'{x=}, {y=}, {f=}, {facing[f]}')
    return abs(x) + abs(y)


def part1(data):
    return walk_path(item.strip() for item in next(data).split(','))


def part2(data):
    return walk_path2(item.strip() for item in next(data).split(','))


def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
