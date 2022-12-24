import fileinput
from helper import *


def parse_input(data):
    lines = list(data)

    grid = {}

    # print(f'{lines[-1].strip()}')

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


def calc_coords(cube_index, location):
    if cube_index == 1:
        return location + (50, 0)
    if cube_index == 2:
        return location + (100, 0)
    if cube_index == 3:
        return location + (50, 50)
    if cube_index == 4:
        return location + (50, 100)
    if cube_index == 5:
        return location + (0, 100)
    if cube_index == 6:
        return location + (0, 150)


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


def find_next_location(facing):
    pass

def next_face(face, facing):
    '''
     12
     3
    54
    6
    '''
    return {
        (1, 'U'): (6, 'R', [[0, 0], [0, 0]]),
        (1, 'R'): (2, 'R', [[1, 0], [0, 1]]),
        (1, 'L'): (5, 'R', [[0, 0], [0, 0]]),
        (1, 'D'): (3, 'D', [[1, 0], [0, 1]]),
        (2, 'U'): (6, 'R', [[0, 0], [0, 0]]),
        (2, 'R'): (2, 'R', [[0, 0], [0, 0]]),
        (2, 'L'): (6, 'R', [[0, 0], [0, 0]]),
        (2, 'D'): (3, 'D', [[0, 0], [0, 0]]),
        (3, 'U'): (6, 'R', [[0, 0], [0, 0]]),
        (3, 'R'): (2, 'R', [[0, 0], [0, 0]]),
        (3, 'L'): (6, 'R', [[0, 0], [0, 0]]),
        (3, 'D'): (3, 'D', [[0, 0], [0, 0]]),
        (4, 'U'): (6, 'R', [[0, 0], [0, 0]]),
        (4, 'R'): (2, 'R', [[0, 0], [0, 0]]),
        (4, 'L'): (6, 'R', [[0, 0], [0, 0]]),
        (4, 'D'): (3, 'D', [[0, 0], [0, 0]]),
        (5, 'U'): (6, 'R', [[0, 0], [0, 0]]),
        (5, 'R'): (2, 'R', [[0, 0], [0, 0]]),
        (5, 'L'): (6, 'R', [[0, 0], [0, 0]]),
        (5, 'D'): (3, 'D', [[0, 0], [0, 0]]),
        (6, 'U'): (6, 'R', [[0, 0], [0, 0]]),
        (6, 'R'): (2, 'R', [[0, 0], [0, 0]]),
        (6, 'L'): (6, 'R', [[0, 0], [0, 0]]),
        (6, 'D'): (3, 'D', [[0, 0], [0, 0]]),


    }


def find_next(cube, face, location, facing):
    while True:
        move = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}[facing]

        if location + move in cube[face]:
            yield location + move, face, facing
        elif face == 1:
            pass


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


def calc_change(facing):
    if facing == 'U':
        return (0, -1)
    elif facing == 'D':
        return (0, 1)
    elif facing == 'L':
        return (-1, 0)
    elif facing == 'R':
        return (1, 0)

def transform(cube, location, next_spot, facing):
    if cube == 1 and facing == 'U':
        return Point(0, location.x), 'R', 6
    elif cube == 1 and facing == 'D':
        return Point(location.x, 0), 'D', 3
    elif cube == 1 and facing == 'R':
        return Point(0, location.y), 'R', 2
    elif cube == 1 and facing == 'L':
        return Point(0, 49 - location.y), 'R', 5
    elif cube == 2 and facing == 'U':
        return Point(location.x, 49), 'U', 6
    elif cube == 2 and facing == 'L':
        return Point(49, location.y), 'L', 1
    elif cube == 2 and facing == 'D':
        return Point(49, location.x), 'L', 3
    elif cube == 2 and facing == 'R':
        return Point(49, 49-location.y), 'L', 4
    elif cube == 3 and facing == 'U':
        return Point(location.x, 49), 'U', 1
    elif cube == 3 and facing == 'L':
        return Point(location.y, 0), 'D', 5
    elif cube == 3 and facing == 'D':
        return Point(location.x, 0), 'D', 4
    elif cube == 3 and facing == 'R':
        return Point(location.y, 49), 'U', 2
    elif cube == 4 and facing == 'U':
        return Point(location.x, 49), 'U', 3
    elif cube == 4 and facing == 'L':
        return Point(49, location.y), 'L', 5
    elif cube == 4 and facing == 'D':
        return Point(49, location.x), 'L', 6
    elif cube == 4 and facing == 'R':
        return Point(49, 49 - location.y), 'L', 2
    elif cube == 5 and facing == 'R':
        return Point(0, location.y), 'R', 4
    elif cube == 5 and facing == 'L':
        return Point(0, 49 - location.y), 'R', 1
    elif cube == 5 and facing == 'D':
        return Point(location.x, 0), 'D', 6
    elif cube == 5 and facing == 'U':
        return Point(0, location.x), 'R', 3
    elif cube == 6 and facing == 'U':
        return Point(location.x, 49), 'U', 5
    elif cube == 6 and facing == 'D':
        return Point(location.x, 0), 'D', 2
    elif cube == 6 and facing == 'L':
        return Point(location.y, 0), 'D', 1
    elif cube == 6 and facing == 'R':
        return Point(location.y, 49), 'U', 4
    raise ValueError(f'{cube=} {location=} {next_spot=} {facing=}')


def transform_facing(cube_index, facing):
    if cube_index in (1, 2, 3, 4):
        return facing
    elif cube_index in (5,):
        return {'U': 'D', 'L': 'R', 'R': 'L', 'D': 'U'}[facing]
    elif cube_index in (6,):
        return {'U': 'L', 'L': 'U', 'R': 'D', 'D': 'R'}[facing]
    else:
        raise ValueError(cube_index, facing)



def part2(data):
    instructions, grid = parse_input(data)

    # print(instructions)

    # location = min(point for point in grid.keys() if point.y == 1)
    location = Point(0, 0) #min(point for point in grid.keys() if point.y == 1)
    facing = 'R'
    cube_index = 1
    cube_size = 50
    print(f'start: {location}')


    print(f'{cube_size=}')

    print(f'max x: {max((point for point in grid.keys()), key=lambda p: p.x)}')
    print(f'min x: {min((point for point in grid.keys()), key=lambda p: p.x)}')
    print(f'max y: {max((point for point in grid.keys()), key=lambda p: p.y)}')
    print(f'min y: {min((point for point in grid.keys()), key=lambda p: p.y)}')
    # build_cube(grid, location.x // 2)
    cube = build_cube(grid, cube_size)

    print([len(cube[i]) for i in range(1, 7)])

    facing = 'R'

    for index, instruction in enumerate(instructions, start=1):
        # print(f'{location=}')
        # print(f'{instruction=}')
        try:
            distance = int(instruction)
            # print(f'moving {distance}')
        except:
            distance = None

        if distance:

            traveled = 0
            while traveled < distance:
                next_spot = location + calc_change(facing)

                if next_spot not in cube[cube_index]:
                    print(f'{cube_index} {facing}')
                    next_spot, next_facing, next_cube_index = transform(cube_index, location, next_spot, facing)

                    if cube[next_cube_index][next_spot] == '#':
                        break
                    else:
                        facing = next_facing
                        cube_index = next_cube_index
                    print(f'{cube_index} {facing}')
                    pass
                elif cube[cube_index][next_spot] == '#':
                    # print('hit wall')
                    break

                location = next_spot
                traveled += 1

        else:
            if instruction == 'L':
                facing = rotate(facing, instruction)
            elif instruction == 'R':
                facing = rotate(facing, instruction)

        print(f'{index:3d}. location={tuple(calc_coords(cube_index, location))} move={instruction} facing={facing, transform_facing(cube_index, facing)}\t\tlocation={location} cube={cube_index}')

        if index % 1000 == 0 and index >= 3000:
            pass
            input()

    print(f'final location = {location}')

    return score(location, facing)


def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
