import fileinput


def parse_grid(lines):
    return {(x, y): h for y, row in enumerate(lines) for x, h in enumerate(row)}


def get_neighboors(x, y):
    for dx in (-1, 1):
        yield (x + dx, y)
    for dy in (-1, 1):
        yield (x, y + dy)


def find_low_points(grid):
    low_points = []

    for location, height in grid.items():
        if all(
            grid.get(neighboor, 10) > height for neighboor in get_neighboors(*location)
        ):
            low_points.append((location, height))

    return low_points


def part1(lines):
    grid = parse_grid(lines)
    low_points = [height for _, height in find_low_points(grid)]

    return sum(low_points) + len(low_points)


def find_basin(grid, basin):
    location = basin[-1]

    for neighboor in get_neighboors(*location):
        if neighboor not in basin and grid.get(neighboor, 9) < 9:
            basin.append(neighboor)
            find_basin(grid, basin)

    return basin


def part2(lines):
    grid = parse_grid(lines)
    low_points = [location for location, _ in find_low_points(grid)]

    basins = [find_basin(grid, [low_point]) for low_point in low_points]

    sizes = list(sorted(map(len, basins)))

    return sizes[-1] * sizes[-2] * sizes[-3]


def main():
    with fileinput.input() as input:
        lines = [[int(location) for location in line.rstrip()] for line in input]

    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
