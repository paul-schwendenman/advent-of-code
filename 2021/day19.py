import fileinput
from collections import namedtuple

class Point(namedtuple('Point', 'x y z')):
    __slots__ = ()

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1], self.z + other[2])

    def __sub__(self, other):
        return Point(self.x - other[0], self.y - other[1], self.z - other[2])

    def __rsub__(self, other):
        return Point(other[0] - self.x, other[1] - self.y, other[2] - self.z)


def transform_point(point):
    x, y, z = point

    for i in (-1, 1):
        for j in (-1, 1):
            for k in (-1, 1):
                yield (i * x, j * y, k * z)
                yield (i * y, j * z, k * x)
                yield (i * z, j * x, k * y)
                yield (i * x, j * z, k * y)
                yield (i * y, j * x, k * z)
                yield (i * z, j * y, k * x)


def transform_points(points):
    yield from zip(*(transform_point(point) for point in points))


def find_matches(beacon_a, scanner_b):
    for _, orientation in enumerate(transform_points(scanner_b[1])):
        m = match(beacon_a, orientation)

        if m:
            pass


def match(beacons_a, beacons_b):
    pass
    for i, beacon_a in enumerate(beacons_a):
        for j, beacon_b in enumerate(beacons_b[i:]):
            offset = beacon_a - beacon_b

            set_a = set(beacons_a)
            set_b = set(beacon + offset for beacon in beacons_b)

            print(f'set_a: {set_a}\nset_b: {set_b}')

            if len(set_a & set_b) >= 12:
                print('mathc')

def parse_scanner(data):
    lines = data.split('\n')

    # print(lines[0])
    number = lines[0].split(' ')[2]

    beacons = [Point(*map(int, line.split(','))) for line in lines[1:]]

    return number, beacons



def part1(lines):
    data = "".join(lines).rstrip()
    raw_scanners = data.split('\n\n')
    scanners = [parse_scanner(item) for item in raw_scanners]

    print(f'scanners: {len(scanners)}')
    print(f'total beacons: {sum(len(scanner[1]) for scanner in scanners)}')
    print(f'max beacons: {sum(len(scanner[1]) for scanner in scanners) - (12 * (len(scanners) - 1))}')

    print(len(set(transform_point((1, 100, 32)))))

    for i, scanner in enumerate(scanners[1:2]):
        _, beacon_a = scanner

        for j in range(i):
            print(f'checking {i} and {j}')
            if find_matches(beacon_a, scanners[j]):
                pass

def part2(data):
    pass


def main():
    with fileinput.input() as input:
        data = [line for line in input]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
