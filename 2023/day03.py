import fileinput
import re
from collections import defaultdict, namedtuple
from itertools import count


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def get_neighbors(self):
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
            yield self + offset

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])


def part1(data):
    grid = defaultdict(str)
    symbols: list[Point] = []
    lines = list(data)

    for y, line in enumerate(lines):
        for x, space in enumerate(line.strip()):
            loc = Point(x, y)
            grid[loc] = space

            if space == '.' or space.isdigit():
                pass
            else:
                symbols.append(loc)

    print(symbols)

    acc = 0

    for symbol in symbols:
        print(f'{symbol=} {grid[symbol]}')
        labels = set()
        for neighbor in (neighbors := symbol.get_neighbors()):
            if grid[neighbor].isdigit():
                print(f'{neighbor=} {grid[neighbor]}')
                if True or (next_neighbor := neighbor + (1, 0)) not in neighbors or (not grid.get(next_neighbor, '.').isdigit()):
                    for j in count(neighbor.x):
                        if not grid.get((j, neighbor.y), '').isdigit():
                            break

                    slice = lines[neighbor.y][:j]
                    print(f'{slice=}')
                    # print(re.match(r'(?:[0-9.]*\.+){0,1}(\d+)$', slice))
                    print(num := int(re.match(r'(?:.*[^0-9]+){0,1}(\d+)$', slice).groups()[0]))

                    # num = int(re.match(r'\.*(\d+)', slice).groups()[0])
                    # print(num)
                    # acc += num
                    labels.add(num)

                else:
                    print('skip')
        print(f'{labels=} {sum(labels)=}')
        acc += sum(labels)

    # print(f'{grid=}')
    return acc


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
