import fileinput
from collections import namedtuple
from itertools import combinations


class Scanner(namedtuple('Scanner', 'number beacons')):
    __slots__ = ()


class Point(namedtuple('Point', 'x y z')):
    __slots__ = ()

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1], self.z + other[2])

    def __sub__(self, other):
        return Point(self.x - other[0], self.y - other[1], self.z - other[2])

    def __rsub__(self, other):
        return Point(other[0] - self.x, other[1] - self.y, other[2] - self.z)

    def __mul__(self, other):
        return Point(other[0] * self.x, other[1] * self.y, other[2] * self.z)


def parse_scanner(data):
    lines = data.split('\n')

    number = lines[0].split(' ')[2]

    beacons = [Point(*map(int, line.split(','))) for line in lines[1:]]

    return Scanner(number, beacons)


def transform_point(point):
    x, y, z = point

    for i in (-1, 1):
        for j in (-1, 1):
            for k in (-1, 1):
                yield Point(x, y, z) * (i, j, k)
                yield Point(y, z, x) * (i, j, k)
                yield Point(z, x, y) * (i, j, k)
                yield Point(x, z, y) * (i, j, k)
                yield Point(y, x, z) * (i, j, k)
                yield Point(z, y, x) * (i, j, k)


def orientations(beacons):
    yield from zip(*(transform_point(beacon) for beacon in beacons))


def match(beacon_a, scanner_b):
    for beacons_b in orientations(scanner_b):
        dm = det_match(beacon_a, beacons_b)
        if dm is not None:
            return [dm + c for c in beacons_b], dm


def det_match(beacons_a, beacons_b):
    for i in range(len(beacons_a)):
        for j in range(i):
            diff = beacons_a[i] - beacons_b[j]
            if commons(beacons_a, beacons_b, diff) >= 12:
                return diff

    return None


def c_sum(x, y):
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])


def c_diff(x, y):
    return (x[0] - y[0], x[1] - y[1], x[2] - y[2])


def commons(beacons_a, beacons_b, diff):
    s = set(beacons_a)

    for beacon in beacons_b:
        s.add(c_sum(beacon, diff))

    return len(beacons_a) + len(beacons_b) - len(s)


def full_match(scanners):
    rotated, remaining = scanners[:1], scanners[1:]
    diffs = []

    while len(remaining):
        print("steps left:", len(remaining))
        step_match(remaining, rotated, diffs)

    return rotated, diffs

def step_match(scanners, rotated_scanners, diffs):
    for e, i in enumerate(scanners):
        for j in rotated_scanners:
            vals = match(j, i)
            if vals is not None:
                mch, diff = vals
                rotated_scanners.append(mch)
                scanners.pop(e)
                diffs.append(diff)
                return

def part1(lines):
    data = "".join(lines).rstrip()
    raw_scanners = data.split('\n\n')
    scanners = [parse_scanner(item) for item in raw_scanners]

    mapped, diffs = full_match([scanner.beacons for scanner in scanners])

    print(diffs)

    beacons = set()

    for view in mapped:
        for point in view:
            beacons.add(point)

    return len(beacons)


def manhatten_distance(x, y):
    a, b, c = x
    d, e, f = y

    return abs(a - d) + abs(b - e) + abs(c - f)


def part2(lines):
    data = "".join(lines).rstrip()
    raw_scanners = data.split('\n\n')
    scanners = [parse_scanner(item) for item in raw_scanners]

    mapped, scanner_locations = full_match([beacons for _, beacons in scanners])
    beacons = set()

    for view in mapped:
        for point in view:
            beacons.add(point)

    return max(manhatten_distance(scanner_a, scanner_b) for scanner_a, scanner_b in combinations(scanner_locations, 2))


def main():
    with fileinput.input() as input:
        data = [line for line in input]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
