import fileinput
from helper import *


def parse_input(data):
    lines = list(data)

    grid = {}

    print(f'{lines[-1].strip()}')

    instructions = re.findall(r'([0-9]+|L|R)', lines[-1].rstrip())

    for y, line in enumerate(lines[:-2], start=0):
        for x, value in enumerate(line.rstrip(), start=0):
            if value in ('.', '#'):
                grid[Point(x,y)] = value

    return instructions, grid


def build_cube(grid, cube_size):
    cube = defaultdict(dict)

    for y in range(0, cube_size):
        for x in range(0, cube_size):
            cube[1][Point(x, y)] = grid[(x + cube_size, y)]
            cube[2][Point(x, y)] = grid[(x + cube_size * 2, y)]
            cube[3][Point(x, y)] = grid[(x + cube_size, y + cube_size)]
            cube[4][Point(x, y)] = grid[(x + cube_size, y + cube_size * 2)]
            cube[5][Point(x, y)] = grid[(x, y + cube_size * 2)]
            cube[6][Point(x, y)] = grid[(x, y + cube_size * 3)]

    return cube


def find_row(grid, location, reverse=False):
    print(sorted((point for point in grid if point.y == location.y), reverse=reverse))
    return cycle(sorted((point for point in grid if point.y == location.y), reverse=reverse))


def find_column(grid, location, reverse=False):
    return cycle(sorted((point for point in grid if point.x == location.x), reverse=reverse))


def rotate(facing, direction):
    if direction == 'L':
        if facing == 'U':
            return 'L'
        if facing == 'D':
            return 'R'
        if facing == 'L':
            return 'D'
        if facing == 'R':
            return 'U'
    elif direction == 'R':
        if facing == 'U':
            return 'R'
        if facing == 'D':
            return 'L'
        if facing == 'L':
            return 'U'
        if facing == 'R':
            return 'D'
    else:
        raise ValueError(direction)


def next_face(face, facing):
    '''
     12
     3
    54
    6
    '''
    return {
        (1, 'U'): (6, 'R'),
        (1, 'R'): (2, 'R'),
        (1, 'L'): (6, 'R'),
        (1, 'D'): (3, 'D'),
        (2, 'U'): (6, 'R'),
        (2, 'R'): (2, 'R'),
        (2, 'L'): (6, 'R'),
        (2, 'D'): (3, 'D'),
        (3, 'U'): (6, 'R'),
        (3, 'R'): (2, 'R'),
        (3, 'L'): (6, 'R'),
        (3, 'D'): (3, 'D'),


    }


def find_next(cube, face, location, facing):
    while True:
        move = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}[facing]

        if location + move in cube[face]:
            yield location + move, face, facing
        elif face == 1:








def score(location, facing):
    facing_score = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
    return location.y * 1000 + location.x * 4 + facing_score[facing]

def part1(data):
    instructions, grid = parse_input(data)

    print(instructions)

    location = min(point for point in grid.keys() if point.y == 1)
    print(f'start: {location}')
    facing = 'R'

    for instruction in instructions:
        print(f'{location=}')
        print(f'{instruction=}')
        try:
            distance = int(instruction)
            print(f'moving {distance}')
        except:
            distance = None

        if distance:
            if facing in ('U', 'D'):
                pathway = find_column(grid, location, reverse=facing=='U')

            else:
                pathway = find_row(grid, location, reverse=facing=='L')
            while (space := next(pathway)) != location:
                print(f'{space} {location}')
                pass

            traveled = 0
            while traveled < distance:
                space = next(pathway)
                print(f'{space=} {grid[space]=}')

                if grid[space] == '#':
                    break
                elif grid[space] == '.':
                    location = space
                    traveled += 1
        else:
            if instruction == 'L':
                facing = rotate(facing, instruction)
            elif instruction == 'R':
                facing = rotate(facing, instruction)

    print(f'final location = {location}')

    return score(location, facing)


def part2(data):
    instructions, grid = parse_input(data)

    # print(instructions)

    location = min(point for point in grid.keys() if point.y == 1)

    cube_size = location.x

    print(f'{cube_size=}')

    print(f'max x: {max((point for point in grid.keys()), key=lambda p: p.x)}')
    print(f'min x: {min((point for point in grid.keys()), key=lambda p: p.x)}')
    print(f'max y: {max((point for point in grid.keys()), key=lambda p: p.y)}')
    print(f'min y: {min((point for point in grid.keys()), key=lambda p: p.y)}')
    # build_cube(grid, location.x // 2)
    cube = build_cube(grid, cube_size)

    print([len(cube[i]) for i in range(1, 7)])

    print(f'start: {location}')
    facing = 'R'

    # for instruction in instructions:
    #     print(f'{location=}')
    #     print(f'{instruction=}')
    #     try:
    #         distance = int(instruction)
    #         print(f'moving {distance}')
    #     except:
    #         distance = None

    #     if distance:
    #         if facing in ('U', 'D'):
    #             pathway = find_column(grid, location, reverse=facing=='U')

    #         else:
    #             pathway = find_row(grid, location, reverse=facing=='L')
    #         while (space := next(pathway)) != location:
    #             print(f'{space} {location}')
    #             pass

    #         traveled = 0
    #         while traveled < distance:
    #             space = next(pathway)
    #             print(f'{space=} {grid[space]=}')

    #             if grid[space] == '#':
    #                 break
    #             elif grid[space] == '.':
    #                 location = space
    #                 traveled += 1
    #     else:
    #         if instruction == 'L':
    #             facing = rotate(facing, instruction)
    #         elif instruction == 'R':
    #             facing = rotate(facing, instruction)

    # print(f'final location = {location}')

    return score(location, facing)


def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
