import fileinput
from collections import defaultdict, namedtuple

class Region(namedtuple('Region', 'x_min x_max y_min y_max z_min z_max')):
    __slots__ = ()

    @property
    def volume(self):
        return abs(self.x_max - self.x_min) * abs(self.y_max - self.y_min) * abs(self.z_max - self.z_min)

    def intersection(self, other):
        x_min = max(self.x_min, other.x_min)
        x_max = min(self.x_max, other.x_max)
        y_min = max(self.y_min, other.y_min)
        y_max = min(self.y_max, other.y_max)
        z_min = max(self.z_min, other.z_min)
        z_max = min(self.z_max, other.z_max)

        if x_max < x_min or y_max < y_min or z_max < z_min:
            return Region(0, 0, 0, 0, 0, 0)

        return Region(x_min, x_max, y_min, y_max, z_min, z_max)


def part1(data: list[str]) -> int:
    #on x=10..12,y=10..12,z=10..12
    #on x=11..13,y=11..13,z=11..13
    #off x=9..11,y=9..11,z=9..11
    #on x=10..10,y=10..10,z=10..10

    grid = defaultdict(bool)

    for line in data:
        command, rest = line.split(' ')
        parts = rest.split(',')

        x_min, x_max = map(int, parts[0][2:].split('..'))
        y_min, y_max = map(int, parts[1][2:].split('..'))
        z_min, z_max = map(int, parts[2][2:].split('..'))

        x_min = max(-50, x_min)
        x_max = min(50, x_max)
        y_min = max(-50, y_min)
        y_max = min(50, y_max)
        z_min = max(-50, z_min)
        z_max = min(50, z_max)

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                for z in range(z_min, z_max + 1):
                    if command == 'on':
                        grid[(x, y, z)] = True
                    else:
                        grid[(x, y, z)] = False

    print(f'x min: {min(item[0] for item in grid.keys())}')
    print(f'x max: {max(item[0] for item in grid.keys())}')
    print(f'y min: {min(item[1] for item in grid.keys())}')
    print(f'y max: {max(item[1] for item in grid.keys())}')
    print(f'z min: {min(item[2] for item in grid.keys())}')
    print(f'z max: {max(item[2] for item in grid.keys())}')

    return sum(1 for value in grid.values() if value)

    pass

def find_new_volume(region: Region, command,  prev_regions: list[tuple[Region, bool]]):
    print(f'region: {region} \t{region.volume} \t{command}')

    volume = region.volume
    intersections = []

    for prev_region, prev_command in prev_regions:
        intersection = region.intersection(prev_region)

        if intersection.volume > 0:
            intersections.append((intersection, prev_command))

    for index, (intersecting_region, prev_command) in enumerate(intersections):
        volume -= find_new_volume(intersecting_region, prev_command, prev_regions=intersections[:index])

    print(f'region: {region} \t{volume}\t=\t{region.volume}\t-\t{region.volume - volume}')

    return volume


def part2(data: list[str]) -> int:
    total = 0
    regions: list[tuple[Region, bool]] = []

    for line in data[:5]:

        command, rest = line.split(' ')
        parts = rest.split(',')

        x_min, x_max = map(int, parts[0][2:].split('..'))
        y_min, y_max = map(int, parts[1][2:].split('..'))
        z_min, z_max = map(int, parts[2][2:].split('..'))

        regions.append((Region(x_min, x_max, y_min, y_max, z_min, z_max), command=='on'))

    for step, (region, command) in enumerate(regions):
        print(f'step {step}')

        if command:
            total += find_new_volume(region, command, regions[:step])

    return total


def main():
    with fileinput.input() as input:
        data = [line.rstrip() for line in input]

    # print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
