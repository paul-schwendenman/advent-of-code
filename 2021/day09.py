import fileinput
from functools import reduce, lru_cache

def get_neighboors(x, y):
    for dx in (-1, 1):
        yield (x + dx, y)
    for dy in (-1, 1):
        yield (x, y + dy)


def part1(lines):
    grid = {}
    low_points = []
    # parse_grid()

    for y, row in enumerate(lines):
        for x, location in enumerate(row):
            grid[(x,y)] = location

    print(grid)

    for y, row in enumerate(lines):
        for x, location in enumerate(row):
            # print((x, y), location, [grid.get(neighboor, 0) < location for neighboor in get_neighboors(x, y)])
            if all(grid.get(neighboor, 1000) > location for neighboor in get_neighboors(x, y)):
                # print((x, y), location, [(grid.get(neighboor, 1000) > location, grid.get(neighboor), neighboor) for neighboor in get_neighboors(x, y)])
                low_points.append(location)


    # low_points = find_low_points()

    return sum(low_points) + len(low_points)


@lru_cache(maxsize=10_000_000)
def find_basin(location, grid, path=[]):
    if location not in grid:
        return set()
    if grid[location] == 9:
        return set()
    if location in path:
        return set()

    return set((location,)) | reduce(lambda a, b: a | b, (find_basin(neighboor, grid, path+[location]) for neighboor in get_neighboors(*location)))


def part2(lines):
    grid = {}
    low_points = []
    # parse_grid()

    for y, row in enumerate(lines):
        for x, location in enumerate(row):
            grid[(x,y)] = location

    # print(grid)

    for y, row in enumerate(lines):
        for x, location in enumerate(row):
            if all(grid.get(neighboor, 1000) > location for neighboor in get_neighboors(x, y)):
                low_points.append((x, y))


    # low_points = find_low_points()
    basins = [find_basin(low_point) for low_point in low_points]

    sizes = list(sorted(map(len, basins)))
    print(sizes)

    return sizes[-1] * sizes[-2] * sizes[-3]


def main():
    with fileinput.input() as input:
        lines = [[int(location) for location in line.rstrip()] for line in input]

    # print(part1(lines))
    print(part2(lines))

if __name__ == '__main__':
    main()