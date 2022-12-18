import fileinput
from helper import *
from tqdm import *

class Rock:
    def __init__(self, pieces, start):
        self.pieces = pieces
        self.pieces = self.calc_move(start)
        self.position = start
        self.width = max(piece.x for piece in pieces)
        self.height = max(piece.y for piece in pieces)

    def move(self, shift):
        if self.check_move(shift):
            # print(f'moving {shift=} {self.pieces}')
            self.pieces = self.calc_move(shift)
            self.position += shift
        else:
            pass
            # print(f'skippin {shift=} {self.pieces}')

        return self.pieces

    def check_move(self, shift):
        if shift[0] + self.position.x + self.width > 7:
            return False
        elif shift[0] + self.position.x < 1:
            return False

        return True

    def calc_move(self, shift):
        return {piece + shift for piece in self.pieces}


def parse_gust(str):
    return (1, 0) if str == '>' else (-1, 0)


def parse_rocks():
    return [
        [
            Point(0, 0),
            Point(1, 0),
            Point(2, 0),
            Point(3, 0),
        ],
        [
            Point(0, 1),
            Point(1, 0),
            Point(1, 1),
            Point(1, 2),
            Point(2, 1),
        ],
        [
            Point(0, 0),
            Point(1, 0),
            Point(2, 0),
            Point(2, 1),
            Point(2, 2),
        ],
        [
            Point(0, 0),
            Point(0, 1),
            Point(0, 2),
            Point(0, 3),
        ],
        [
            Point(0, 0),
            Point(0, 1),
            Point(1, 0),
            Point(1, 1)
        ]
    ]

def part1(data):
    gusts = cycle(next(data).strip())
    rocks = parse_rocks()
    grid = set(Point(x, 0) for x in range(1, 8))

    height = 1

    for _index, rock_base in tqdm(zip(range(1, 2023), cycle(rocks))):
        start = Point(3, height + 3)
        rock = Rock(rock_base, start)

        # print(f'----------- {index} ----------')
        # print_grid(grid, rock.pieces, height=height)
        # input()

        for j in count():
            gust = parse_gust(next(gusts))
            if not (rock.calc_move(gust) & grid):
                rock.move(gust)

            down = (0, -1)

            if rock.calc_move(down) & grid:
                # print(rock.calc_move(down) & grid)
                grid |= rock.pieces
                break
            else:
                rock.move(down)

            # print_grid(grid, rock.pieces, height=height)
            # input()


            # print(f'{j=}')

        # print_grid(grid)
        # input()

        height = max(p.y for p in grid) + 1
    # print_grid(grid, height - 20)
    return height - 1


def print_grid(grid, rock=set(), height=0):
    for y in range(6 + height, max(height - 14, -1), -1):
        print(f'{y:4d}\t |', end='')
        for x in range(1, 8):
            print('@' if ((x, y) in rock) else ('#' if (x, y) in grid else '.'), end='')
        print('|')
    # if height <= 1:
    #     print(''.join('-' if (x, 0) in grid else '+' for x in range(0, 9)))



def part2(data):
    gusts = cycle(next(data).strip())
    rocks = parse_rocks()
    grid = set(Point(x, 0) for x in range(1, 8))

    height = 1

    for _index, rock_base in tqdm(zip(range(1_000_000_000_000), cycle(rocks)), total=1_000_000_000_000):
        start = Point(3, height + 3)
        rock = Rock(rock_base, start)

        for j in count():
            gust = parse_gust(next(gusts))
            if not (rock.calc_move(gust) & grid):
                rock.move(gust)

            down = (0, -1)

            if rock.calc_move(down) & grid:
                grid |= rock.pieces
                break
            else:
                rock.move(down)

        height = max(p.y for p in grid) + 1
    return height - 1


def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
