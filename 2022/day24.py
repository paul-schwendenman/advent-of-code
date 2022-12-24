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
    blizzards = defaultdict(list)

    for y, line in enumerate(data, start=1):
        for x, value in enumerate(line.rstrip(), start=1):
            if value in ('#', '.'):
                grid[Point(x, y)] = value
            if value in ('<', '>', '^', 'v'):
                blizzards[value].append(Point(x, y))
                grid[Point(x, y)] = '.'

    return grid, blizzards


@cache
def move_blizzards(cachable, min_x, max_x, min_y, max_y):
    offset = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}

    new_blizzards = defaultdict(list)

    for direction, blizzards in cachable:
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


@cache
def in_blizzard(all_blizzards, location):
    return any(location in blizzards for blizzards in all_blizzards)


def cache_blizzards(blizzards):
    return tuple((key, tuple(value)) for key, value in blizzards.items())


def replay(grid, initial_blizzards, path):
    blizzard = initial_blizzards
    max_x = max((point.x for point in grid.keys()))
    min_x = min((point.x for point in grid.keys()))
    max_y = max((point.y for point in grid.keys()))
    min_y = min((point.y for point in grid.keys()))

    for location in path:
        print(f'---- {location} ----')
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if (x, y) in grid and grid[(x, y)] == '#':
                    if (x,y) == location:
                        raise ValueError
                    print('#', end='')
                elif Point(x, y) == location:
                    print('E', end='')
                elif (x,y) in blizzard['>']:
                    print('>', end='')
                elif (x,y) in blizzard['<']:
                    print('<', end='')
                elif (x,y) in blizzard['^']:
                    print('^', end='')
                elif (x,y) in blizzard['v']:
                    print('v', end='')
                else:
                    print('.', end='')
            print()
        cachable_blizzards = cache_blizzards(blizzard)
        blizzard = move_blizzards(cachable_blizzards, min_x=min_x, max_x=max_x, min_y=min_y, max_y=max_y)
        print()

def part1(data):
    grid, blizzards = parse_input(data)
    location = Point(2, 1)

    max_x = max((point.x for point in grid.keys()))
    min_x = min((point.x for point in grid.keys()))
    max_y = max((point.y for point in grid.keys()))
    min_y = min((point.y for point in grid.keys()))
    # print(f'{min_x}-{max_x} {min_y}-{max_y}')

    goal = Point(max_x - 1, max_y)

    replay(grid, blizzards, [location, (2,2)])

    states = [State.build((location,), blizzards, goal, 0)]
    heapify(states)

    max_t = 0
    best_t = inf
    best = {}

    while states:
        state = heappop(states)
        cachable_blizzards = cache_blizzards(state.blizzards)
        new_blizzards = move_blizzards(cachable_blizzards, min_x=min_x, max_x=max_x, min_y=min_y, max_y=max_y)

        if best_t < state.time:
            continue

        if (state.location, combined := frozenset(chain.from_iterable(new_blizzards.values()))) in best:
            continue

        best[(state.location, combined)] = state.time

        if max_t < state.time:
            max_t = state.time
            print(max_t, len(states))

        if goal == state.location:
            best_t = state.time
            print(state.path)
            print(f'found! {best_t}')
            break
            # continue

        for next_location in moves(state.location):
            if next_location in grid and grid[next_location] != '#' and not in_blizzard(cache_blizzards(new_blizzards), next_location):
                heappush(states, State.build(state.path + (next_location,), new_blizzards, goal, state.time + 1))


    return best_t
    # for i in count():
    #     print(f'------- step {i} states {len(states)} ----------')
    #     next_states = deque()

    #     while states:
    #         state = states.popleft()
    #         cachable_blizzards = cache_blizzards(blizzards)
    #         new_blizzards = move_blizzards(cachable_blizzards, min_x=min_x, max_x=max_x, min_y=min_y, max_y=max_y)

    #         if (state, combined := frozenset(chain.from_iterable(new_blizzards.values()))) in best:
    #             continue

    #         best[(state, combined)] = i

    #         if state == goal:
    #             return i

    #         for next_state in moves(state):
    #             if next_state in grid and grid[next_state] != '#' and not in_blizzard(cache_blizzards(new_blizzards), next_state):
    #                 next_states.append(next_state)
    #             pass
    #     states = next_states
    #     blizzards = new_blizzards


def part2(data):
    pass


def main():
    try:
        print(part1(fileinput.input()))
    finally:
        print(f'move_blizzards: {move_blizzards.cache_info()}')
        print(f'in_blizzard: {in_blizzard.cache_info()}')
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
