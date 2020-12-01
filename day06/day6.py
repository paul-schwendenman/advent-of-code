from collections import defaultdict


def create_map(orbits):
    orbit_map = defaultdict(list)

    for orbit in orbits:
        parent, child = orbit.split(')')
        orbit_map[parent].append(child)

    return orbit_map


def count_orbits(orbit_map, key="COM", depth=0):
    if key in orbit_map:
        total = sum([count_orbits(orbit_map, child, depth+1) for child in orbit_map[key]])
        return total + depth
    else:
        return depth


def find_path(orbit_map, start="COM", end="YOU"):
    if end in orbit_map[start]:
        return [start]
    else:
        for child in orbit_map[start]:
            path = find_path(orbit_map, child, end)
            if path:
                path.append(start)
                return path
        else:
            return None


def calc_orbits(input):
    return count_orbits(create_map(input))


def calc_hops(lines):
    orbit_map = create_map(lines)

    you_path = set(find_path(orbit_map))
    san_path = set(find_path(orbit_map, end="SAN"))

    return len(you_path.symmetric_difference(san_path))


def main():
    with open('day06/input') as input:
        lines = input.read().splitlines()

    orbits = calc_orbits(lines)

    return orbits


def main2():
    with open('day06/input') as input:
        lines = input.read().splitlines()

    return calc_hops(lines)


if __name__ == "__main__":
    print(main())
    print(main2())
