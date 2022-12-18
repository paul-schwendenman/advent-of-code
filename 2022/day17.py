import fileinput
from helper import *
from tqdm import *

class Rock:
    def __init__(self, pieces, start):
        self.pieces = self.calc_move(pieces)
        self.position = start
        # self.position = start
        self.width = max(piece.x for piece in pieces)
        self.height = max(piece.y for piece in pieces)

    def move(self, shift):
        if self.calc_move(shift):
            print(f'moving {shift=} {self.pieces}')
            self.pieces = self.calc_move(shift)
            print(f'moved {shift=} {self.pieces}')
            self.position += shift

    def check_move(self, shift):
        if shift[0] + self.position.x + self.width > 7:
            return False
        elif shift[0] + self.position.x < 1:
            return False

        return True

    def calc_move(self, shift):
        return {piece + shift for piece in self.pieces}


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
    gusts = next(data).strip()
    gust_size = len(gusts)
    rocks = parse_rocks()
    grid = set(Point(x, 0) for x in range(1, 8))

    height = 1

    for index, rock_base in list(zip(range(2023), cycle(rocks))):
        start = Point(3, height + 3)
        rock = Rock(rock_base, start)

        print_grid(grid | rock.pieces)
        input()

        for j in count():
            if gusts[index % gust_size] == '>':
                rock.move((1, 0))
            else:
                rock.move((-1, 0))

            print_grid(grid | rock.pieces)
            input()

            if (pieces := rock.predict_move((0, -1))) & grid:
                grid |= pieces
                break
            else:
                rock.move((0, -1))

            print_grid(grid | rock.pieces)
            input()


            print(f'{j=}')

        print_grid(grid)
        input()

        height = max(p.y for p in grid)
    return height


def print_grid(grid, height=0):

    for y in range(10  + height, height, -1):
        print('|', end='')
        for x in range(1, 8):
            print('#' if (x, y) in grid else '.', end='')
        print('|')
    if height <= 1:
        print(''.join('-' if (x, 0) in grid else '+' for x in range(0, 9)))



def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
