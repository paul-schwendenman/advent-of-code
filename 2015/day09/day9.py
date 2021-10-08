import fileinput
import itertools
import re

def pair(place_1, place_2):
    if place_1 < place_2:
        return (place_1, place_2)
    else:
        return (place_2, place_1)


def pairwise(route):
    a, b = itertools.tee(route)

    next(b, None)

    return zip(a, b)

def part1(paths):
    places = set()
    distances = {}
    parser = re.compile(r'(?P<place_1>[A-Za-z]+) to (?P<place_2>[A-Za-z]+) = (?P<distance>[0-9]+)')

    for path in paths:
        matches = parser.match(path).groupdict()

        place_1 = matches['place_1']
        place_2 = matches['place_2']
        distance = matches['distance']

        places.add(place_1)
        places.add(place_2)
        distances[pair(place_1, place_2)] = int(distance)

    return min(sum(distances[pair(place_1, place_2)] for place_1, place_2 in pairwise(route)) for route in itertools.permutations(places, len(places)))


def part2(paths):
    places = set()
    distances = {}
    parser = re.compile(r'(?P<place_1>[A-Za-z]+) to (?P<place_2>[A-Za-z]+) = (?P<distance>[0-9]+)')

    for path in paths:
        matches = parser.match(path).groupdict()

        place_1 = matches['place_1']
        place_2 = matches['place_2']
        distance = matches['distance']

        places.add(place_1)
        places.add(place_2)
        distances[pair(place_1, place_2)] = int(distance)

    return max(sum(distances[pair(place_1, place_2)] for place_1, place_2 in pairwise(route)) for route in itertools.permutations(places, len(places)))


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()