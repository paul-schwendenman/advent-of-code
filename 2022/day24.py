import fileinput
from helper import *
from heapq import heapify, heappop, heappush


class State(namedtuple('State', 'score time path blizzards')):
    __slots__ = ()

    @classmethod
    def build(cls, path, blizzards, goal, time):
        return cls(calc_manhatten_distance(goal, path[-1]) + time, time, path, blizzards)

    @property
    def location(self):
        return self.path[-1]

def moves(point):
    for diff in [(0, 0), (1, 0), (-1, 0), (0, -1), (0, 1)]:
        yield point + diff


def parse_input(data):
    grid = {}
    blizzards = defaultdict(tuple)

    for y, line in enumerate(data, start=1):
        for x, value in enumerate(line.rstrip(), start=1):
            if value in ('#', '.'):
                grid[Point(x, y)] = value
            if value in ('<', '>', '^', 'v'):
                blizzards[value] += (Point(x, y),)
                grid[Point(x, y)] = '.'

    return grid, blizzards


@cache
def move_blizzards(cachable, min_x, max_x, min_y, max_y):
    offset = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}

    new_blizzards = defaultdict(tuple)

    for direction, blizzards in cachable:
        for blizzard in blizzards:
            next_blizzard = blizzard + offset[direction]
            if direction == '<' and next_blizzard.x == min_x:
                new_blizzards[direction] += (Point(max_x - 1, next_blizzard.y),)
            elif direction == '>' and next_blizzard.x == max_x:
                new_blizzards[direction] += (Point(min_x + 1, next_blizzard.y),)
            elif direction == '^' and next_blizzard.y == min_y:
                new_blizzards[direction] += (Point(next_blizzard.x, max_y - 1),)
            elif direction == 'v' and next_blizzard.y == max_y:
                new_blizzards[direction] += (Point(next_blizzard.x, min_y + 1),)
            else:
                new_blizzards[direction] += (next_blizzard,)

    return new_blizzards


@cache
def in_blizzard(all_blizzards, location):
    return any(location in blizzards[1] for blizzards in all_blizzards)


def cache_blizzards(blizzards):
    return tuple((key, tuple(value)) for key, value in blizzards.items())


def replay(grid, initial_blizzards, path):
    blizzard = initial_blizzards
    max_x = max((point.x for point in grid.keys()))
    min_x = min((point.x for point in grid.keys()))
    max_y = max((point.y for point in grid.keys()))
    min_y = min((point.y for point in grid.keys()))

    for index, location in enumerate(path):
        print(f'---- {index} {location} ----')
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if (x, y) in grid and grid[(x, y)] == '#':
                    if (x,y) == location:
                        raise ValueError('In wall!')
                    print('#', end='')
                elif len(matching := [dir for dir, spots in blizzard.items() if (x, y) in spots]) > 0:
                    if Point(x, y) == location:
                        print('X', end='')
                    if len(matching) == 1:
                        print(f'{matching[0]}', end='')
                    else:
                        print(f'{len(matching)}', end='')
                elif Point(x, y) == location:
                    print('E', end='')
                else:
                    print('.', end='')
            print()
        cachable_blizzards = cache_blizzards(blizzard)
        blizzard = move_blizzards(cachable_blizzards, min_x=min_x, max_x=max_x, min_y=min_y, max_y=max_y)
        print()


def solve(grid, blizzards, start, goal, min_x, max_x, min_y, max_y):
    states = [State.build((start,), blizzards, goal, 0)]
    heapify(states)

    max_t = 0
    best_t = inf
    best = {}

    while states:
        state = heappop(states)
        cachable_blizzards = cache_blizzards(state.blizzards)
        new_blizzards = move_blizzards(cachable_blizzards, min_x=min_x, max_x=max_x, min_y=min_y, max_y=max_y)

        if best_t <= state.time:
            continue

        if (state.location, combined := frozenset(chain.from_iterable(new_blizzards.values()))) in best:
            continue

        best[(state.location, combined)] = state.time

        if max_t < state.time:
            max_t = state.time
            print(f'{max_t=}, # of states: {len(states)}, first: {states[0].time}, last: {states[-1].score} {set((state.score) for state in states)}')

        if goal == state.location:
            best_t = state.time
            # replay(grid, blizzards, state.path)
            print(state.path)
            print(f'found! {best_t}')
            blizzards = state.blizzards
            break
            # continue

        for next_location in moves(state.location):
            if next_location in grid and grid[next_location] != '#' and not in_blizzard(cache_blizzards(new_blizzards), next_location):
                heappush(states, State.build(state.path + (next_location,), new_blizzards, goal, state.time + 1))


    return best_t, blizzards


def part1(data):
    grid, blizzards = parse_input(data)

    max_x = max((point.x for point in grid.keys()))
    min_x = min((point.x for point in grid.keys()))
    max_y = max((point.y for point in grid.keys()))
    min_y = min((point.y for point in grid.keys()))
    # print(f'{min_x}-{max_x} {min_y}-{max_y}')

    end = Point(max_x - 1, max_y)
    start = Point(min_x + 1, min_y)

    return solve(grid, blizzards, start, end, min_x, max_x, min_y, max_y)[0]


def part2(data):
    pass

def main():
    try:
        print(part1(fileinput.input()))
        # print(part2(fileinput.input()))
    finally:
        print(f'move_blizzards: {move_blizzards.cache_info()}')
        print(f'in_blizzard: {in_blizzard.cache_info()}')


if __name__ == '__main__':
    main()
