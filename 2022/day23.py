import fileinput
from helper import *
from tqdm import tqdm


class Elf(namedtuple('Elf', 'x y')):
    __slots__ = ()

    def __add__(self, other):
        return Elf(self.x + other[0], self.y + other[1])

    def neighbors_n(self):
        yield from (self + delta for delta in [(-1, -1), (0, -1), (1, -1)])

    def neighbors_e(self):
        yield from (self + delta for delta in [(1, -1), (1, 0), (1, 1)])

    def neighbors_s(self):
        yield from (self + delta for delta in [(-1, 1), (0, 1), (1, 1)])

    def neighbors_w(self):
        yield from (self + delta for delta in [(-1, -1), (-1, 0), (-1, 1)])

    def neighbors(self):
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                yield self + (dx, dy)


def parse_input(data):
    grid = set()
    for y, line in enumerate(data):
        for x, value in enumerate(line):
            if value == '#':
                grid.add(Elf(x, y))

    return grid


def print_grid(grid):
    min_x = min(point.x for point in grid)
    max_x = max(point.x for point in grid)
    min_y = min(point.y for point in grid)
    max_y = max(point.y for point in grid)

    for y in range(min_y-1, max_y+2):
        for x in range(min_x-1, max_x+2):
            if (x,y) in grid:
                print('#', end='')
            else:
                print('.', end='')
        print('')


def part1(data):
    grid = (parse_input(data))
    total_elves = len(grid)

    print(f'{total_elves}') #grid)

    print_grid(grid)

    directions = deque(['N', 'S', 'W', 'E'])

    for _ in tqdm(range(10)):
        next_locations = defaultdict(list)
        new_grid = set()

        for elf in grid:
            has_neighbors_n = (set(elf.neighbors_n()) & grid)
            has_neighbors_s = (set(elf.neighbors_s()) & grid)
            has_neighbors_w = (set(elf.neighbors_w()) & grid)
            has_neighbors_e = (set(elf.neighbors_e()) & grid)

            # print(f'{elf=} {has_neighbors_n=} {has_neighbors_s=} {has_neighbors_w=} {has_neighbors_e=}')

            if not any([has_neighbors_n, has_neighbors_s, has_neighbors_w, has_neighbors_e]):
                next_locations[elf].append(elf)
            else:
                for direction in directions:
                    # print(f'testing {direction}')
                    if direction == 'N' and not has_neighbors_n:
                        # print('trying north')
                        next_locations[elf + (0, -1)].append(elf)
                        break
                    elif direction == 'S' and not has_neighbors_s:
                        # print('trying south')
                        next_locations[elf + (0, 1)].append(elf)
                        break
                    elif direction == 'W' and not has_neighbors_w:
                        # print('trying west')
                        next_locations[elf + (-1, 0)].append(elf)
                        break
                    elif direction == 'E' and not has_neighbors_e:
                        # print('trying east')
                        next_locations[elf + (1, 0)].append(elf)
                        break
                else:
                    next_locations[elf].append(elf)
                    # raise ValueError

            # print(len(next_locations))

        for location, elves in next_locations.items():
            if len(elves) == 1:
                new_grid.add(location)
            else:
                # print(f'multiple elves: {location} {elves}')
                for elf in elves:
                    new_grid.add(elf)

        directions.rotate(-1)
        # print(f'{len(new_grid)=}') #, new_grid)
        grid = new_grid

        # print_grid(grid)
        assert len(new_grid) == total_elves

        # input()

    min_x = min(point.x for point in grid)
    max_x = max(point.x for point in grid)
    min_y = min(point.y for point in grid)
    max_y = max(point.y for point in grid)

    area = (1 + max_x - min_x) * (1 + max_y - min_y)

    print(f'{min_x=} {max_y=} {min_x=} {max_x=} {area=}')
    # print(sum(1 for point, value in grid.items() if value))

    return area - total_elves
    pass


def part2(data):
    grid = (parse_input(data))
    total_elves = len(grid)

    print(f'{total_elves}') #grid)

    print_grid(grid)

    directions = deque(['N', 'S', 'W', 'E'])

    for i in tqdm(count()):
        next_locations = defaultdict(list)
        new_grid = set()

        for elf in grid:
            has_neighbors_n = (set(elf.neighbors_n()) & grid)
            has_neighbors_s = (set(elf.neighbors_s()) & grid)
            has_neighbors_w = (set(elf.neighbors_w()) & grid)
            has_neighbors_e = (set(elf.neighbors_e()) & grid)

            # print(f'{elf=} {has_neighbors_n=} {has_neighbors_s=} {has_neighbors_w=} {has_neighbors_e=}')

            if not any([has_neighbors_n, has_neighbors_s, has_neighbors_w, has_neighbors_e]):
                next_locations[elf].append(elf)
            else:
                for direction in directions:
                    # print(f'testing {direction}')
                    if direction == 'N' and not has_neighbors_n:
                        # print('trying north')
                        next_locations[elf + (0, -1)].append(elf)
                        break
                    elif direction == 'S' and not has_neighbors_s:
                        # print('trying south')
                        next_locations[elf + (0, 1)].append(elf)
                        break
                    elif direction == 'W' and not has_neighbors_w:
                        # print('trying west')
                        next_locations[elf + (-1, 0)].append(elf)
                        break
                    elif direction == 'E' and not has_neighbors_e:
                        # print('trying east')
                        next_locations[elf + (1, 0)].append(elf)
                        break
                else:
                    next_locations[elf].append(elf)
                    # raise ValueError

            # print(len(next_locations))

        for location, elves in next_locations.items():
            if len(elves) == 1:
                new_grid.add(location)
            else:
                # print(f'multiple elves: {location} {elves}')
                for elf in elves:
                    new_grid.add(elf)

        directions.rotate(-1)
        # print(f'{len(new_grid)=}') #, new_grid)
        if grid == new_grid:
            break
            # return i + 1
        grid = new_grid

        # print_grid(grid)
        assert len(new_grid) == total_elves

        # input()

    # min_x = min(point.x for point in grid)
    # max_x = max(point.x for point in grid)
    # min_y = min(point.y for point in grid)
    # max_y = max(point.y for point in grid)

    # area = (1 + max_x - min_x) * (1 + max_y - min_y)

    # print(f'{min_x=} {max_y=} {min_x=} {max_x=} {area=}')
    # print(sum(1 for point, value in grid.items() if value))

    print()
    return i + 1


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
