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

    return len(tail_locations)


def print_knots(knots, size=15):
    display = 'H123456789'
    for y in range(size, -size, -1):
        for x in range(-size, size):
            if (x, y) in knots:
                print(display[knots.index((x,y))], end="")
            elif (0, 0) == (x, y):
                print('s', end="")
            else:
                print('.', end="")
        print('')


def print_locations(locations, size=15):
    for y in range(size, -size, -1):
        for x in range(-size, size):
            if (0, 0) == (x, y):
                print('s', end="")
            elif (x, y) in locations:
                print("#", end="")
            else:
                print('.', end="")
        print('')


def part2(data):
    knots = [Point(0, 0) for _ in range(10)]
    tail_locations = set([knots[-1]])

    for move in list(get_moves(data))[:]:
        # print(f'\n------- {move} -------\n')
        for _ in range(move.distance):
            knots[0] += calc_offest(move.direction)

            for index, knot in enumerate(knots[1:]):
                # print(index, knots[index], knot, calc_tail_offset(knots[index], knot))
                knots[index+1] = knot + calc_tail_offset(knots[index], knot)
                # print("after:", knots)

            # print_knots(knots, 6)
            # print()


            tail_locations.add(knots[-1])
            # print('-----')
        # print_knots(knots)

    # print('\n --------------------\n')
    # print_locations(tail_locations, 6)

    return len(tail_locations)


def main():
    print(part1(fileinput.input()))
    # assert(part1(fileinput.input()) == 1776)
    print(part2(fileinput.input()))
    # assert(part2(fileinput.input()) == 234416)


if __name__ == '__main__':
    main()
