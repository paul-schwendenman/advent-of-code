from enum import Enum
from collections import namedtuple, defaultdict
from itertools import count
import math
from typing import List, Iterator, Dict


Point = namedtuple('Point', 'x y')
Path = namedtuple('Path', 'count group')
Location = namedtuple('Location', 'coords group')


class MazeItem(Enum):
    ENTRANCE = '@'
    OPEN_PASSAGE = '.'
    STONE_WALL = '#'


def get_neighboors(location: Point) -> Iterator[Point]:
    yield Point(location.x - 1, location.y)
    yield Point(location.x + 1, location.y)
    yield Point(location.x, location.y - 1)
    yield Point(location.x, location.y + 1)


def process_maze(template):
    maze = {}
    goals = {}

    for y, row in enumerate(template):
        for x, item in enumerate(row):
            point = Point(x, y)
            maze[point] = item
            if item not in ('.', '#'):
                goals[item] = point

    return maze, goals


def find_paths(maze, start):
    paths: Dict[str, Path] = {}
    route: Dict[Point, Path] = defaultdict(lambda: Path(math.inf, set()))
    route[start] = Path(0, set())
    next_location: List[Location] = [Location(start, set())]

    for step in count(1):
        if not next_location:
            break

        current_locations, next_location = next_location, []

        for current_location, ds in current_locations:
            for neighboor in get_neighboors(current_location):
                item = maze[neighboor]
                if item == '#' or route[neighboor][0] <= step:
                    continue
                if item.islower():  # Check if key
                    paths[item] = (step, ds)
                new_ds = ds
                if item.isupper():  # Check if door
                    new_ds = new_ds | {item.lower()}
                route[neighboor] = (step, new_ds)
                next_location.append(Location(neighboor, new_ds))

    return paths


def main(filename="input"):
    with open(filename) as input_file:
        grid_template = input_file.read().splitlines()

    maze, goals = process_maze(grid_template)

    keys = {key for key in goals.keys() if key.islower()}
    links = {
        '@': find_paths(maze, goals['@'])
    }

    for key in keys:
        links[key] = find_paths(maze, goals[key])

    cache = {}

    def walk_path(name, need_keys):
        if not need_keys:
            return 0

        cache_key = name + ''.join(need_keys)
        if cache_key in cache:
            return cache[cache_key]

        shortest = math.inf
        for key in need_keys:
            path_length, doors = links[name][key]

            if path_length >= shortest:
                continue

            if not doors.isdisjoint(need_keys):
                continue

            tail = walk_path(key, need_keys - {key})

            if shortest > (path_length + tail):
                shortest = path_length + tail

        cache[cache_key] = shortest
        return shortest

    result = walk_path('@', keys)
    print(f'cached: {len(cache)}')

    return result


def main2(filename="input.part2"):
    with open(filename) as input_file:
        grid_template = input_file.read().splitlines()

    maze, goals = process_maze(grid_template)

    keys = {key for key in goals.keys() if key.islower()}
    links = {
        '1': find_paths(maze, goals['1']),
        '2': find_paths(maze, goals['2']),
        '3': find_paths(maze, goals['3']),
        '4': find_paths(maze, goals['4']),
    }

    for key in keys:
        links[key] = find_paths(maze, goals[key])

    cache = {}

    def walk_path(names, need_keys):
        if not need_keys:
            return 0

        cache_key = ''.join(names) + ''.join(need_keys)
        if cache_key in cache:
            return cache[cache_key]

        shortest = math.inf
        for key in need_keys:
            for name in names:
                if key not in links[name]:
                    continue

                path_length, doors = links[name][key]

                if path_length >= shortest:
                    continue

                if not doors.isdisjoint(need_keys):
                    continue

                tail = walk_path(names - {name} | {key}, need_keys - {key})

                if shortest > (path_length + tail):
                    shortest = path_length + tail

        cache[cache_key] = shortest
        return shortest

    result = walk_path({'1', '2', '3', '4'}, keys)
    print(f'cached: {len(cache)}')

    return result


if __name__ == "__main__":
    print(main2())
