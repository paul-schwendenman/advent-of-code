import fileinput
from collections import namedtuple



Move = namedtuple('Move', 'direction distance')

class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])

    # def move(self, direction):
        # match direction:
        #     case 'U':
        #         return self + (0, 1)
        #     case 'D'
        #         return self + (0, -1)
        #     case 'L':
        #         return self + (-1, 0)
        #     case 'R':
        #         return self + (1, 0)

def calc_offest(direction):
    if direction == 'U':
        return (0, 1)
    elif direction == 'D':
        return (0, -1)
    elif direction == 'L':
        return (-1, 0)
    elif direction == 'R':
        return (1, 0)


def calc_tail_offset(head, tail):
    diff_x = head.x - tail.x
    diff_y = head.y - tail.y

    if abs(diff_x) > 1:
        return diff_x // 2, diff_y

    if abs(diff_y) > 1:
        return diff_x, diff_y // 2

    return (0, 0)


def get_moves(data):
    for line in data:
        direction, distance = line.split(' ')
        yield Move(direction, int(distance))

def part1(data):
    head = Point(0, 0)
    tail = Point(0, 0)
    tail_locations = set([tail])

    for move in get_moves(data):
        for _ in range(move.distance):
            head += calc_offest(move.direction)
            tail += calc_tail_offset(head, tail)
            tail_locations.add(tail)


        print(head, tail)
        pass
    return len(tail_locations)



def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    # assert(part1(fileinput.input()) == 1776)
    print(part2(fileinput.input()))
    # assert(part2(fileinput.input()) == 234416)


if __name__ == '__main__':
    main()
