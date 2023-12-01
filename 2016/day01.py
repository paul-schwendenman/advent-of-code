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
        turn, length = instruction[0], int(instruction[1])

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


def part1(data):
    return walk_path(item.strip() for item in next(data).split(','))


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    # print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
