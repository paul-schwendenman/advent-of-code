import fileinput
from helper import *

def moves(point):
    for diff in [(0, 0), (1, 0), (-1, 0), (0, -1), (0, 1)]:
        yield point + diff

def parse_input(data):
    grid = {}
    blizzards = defaultdict(list)

    for y, line in enumerate(data, start=1):
        for x, value in enumerate(line.rstrip(), start=1):
            if value in ('#', '.'):
                grid[Point(x, y)] = value
            if value in ('<', '>', '^', 'v'):
                blizzards[value].append(Point(x, y))
                grid[Point(x, y)] = '.'

    return grid, blizzards


def move_blizzards(all_blizzards, min_x, max_x, min_y, max_y):
    offset = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
    new_blizzards = defaultdict(list)

    for direction, blizzards in all_blizzards.items():
        for blizzard in blizzards:
            next_blizzard = blizzard + offset[direction]
            if direction == '<' and next_blizzard.x == min_x:
                new_blizzards[direction].append(Point(max_x - 1, next_blizzard.y))
            elif direction == '>' and next_blizzard.x == max_x:
                new_blizzards[direction].append(Point(min_x + 1, next_blizzard.y))
            elif direction == '^' and next_blizzard.y == min_y:
                new_blizzards[direction].append(Point(next_blizzard.x, max_y - 1))
            elif direction == 'v' and next_blizzard.y == max_y:
                new_blizzards[direction].append(Point(next_blizzard.x, min_y + 1))
            else:
                new_blizzards[direction].append(next_blizzard)

    return new_blizzards


def in_blizzard(all_blizzards, location):
    return any(location in blizzards for blizzards in all_blizzards.values())


def part1(data):
    grid, blizzards = parse_input(data)
    location = Point(1, 2)

    max_x = max((point.x for point in grid.keys()))
    min_x = min((point.x for point in grid.keys()))
    max_y = max((point.y for point in grid.keys()))
    min_y = min((point.y for point in grid.keys()))
    # print(f'{min_x}-{max_x} {min_y}-{max_y}')

    goal = Point(max_x - 1, max_y)

    states = deque([location])

    best = {}

    for i in count():
        print(f'------- step {i} states {len(states)} ----------')
        next_states = deque()

        while states:
            state = states.popleft()
            new_blizzards = move_blizzards(blizzards, min_x=min_x, max_x=max_x, min_y=min_y, max_y=max_y)

            if (state, combined := frozenset(chain.from_iterable(new_blizzards.values()))) in best:
                continue

            best[(state, combined)] = i

            if state == goal:
                return i

            for next_state in moves(state):
                if next_state in grid and grid[next_state] != '#' and not in_blizzard(new_blizzards, next_state):
                    next_states.append(next_state)
                pass
        states = next_states
        blizzards = new_blizzards


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
