import fileinput

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
                print((x, y), location, [(grid.get(neighboor, 1000) > location, grid.get(neighboor), neighboor) for neighboor in get_neighboors(x, y)])
                low_points.append(location)


    # low_points = find_low_points()

    return sum(low_points) + len(low_points)


def main():
    with fileinput.input() as input:
        lines = [[int(location) for location in line.rstrip()] for line in input]

    print(part1(lines))

if __name__ == '__main__':
    main()
