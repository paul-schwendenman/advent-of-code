import fileinput


def parse_scanner(data):
    lines = data.split('\n')

    print(lines[0])
    number = lines[0].split(' ')[2]

    beacons = [tuple(map(int, line.split(','))) for line in lines[1:]]

    return number, beacons


def magnitude(b, b2):
    return (b[0] - b2[0]) ** 2 + (b[1] - b2[1]) ** 2 + (b[2] - b2[2]) ** 2


def parse_beacons(beacons):
    magnitudes = {}

    for i in range(len(beacons)):
        b = beacons[i]
        magnitudes[i] = { magnitude(b, b2) for j, b2 in enumerate(beacons) if j != i}

    return list(sorted(magnitudes.values(), key=lambda item: len(item)))[:12]


def part1(lines):
    data = "".join(lines).rstrip()

    raw_scanners = data.split('\n\n')

    scanners = [parse_scanner(item) for item in raw_scanners]

    print(scanners[0])
    print(len(scanners[0][1]))

    # print(parse_beacons(scanners[0][1]))
    # print('--------------')
    # print(parse_beacons(scanners[1][1]))
    # print('--------------')
    # print(parse_beacons(scanners[2][1]))

    beacons1 = parse_beacons(scanners[0][1])

    # print(len([1 for item in beacons2 if item not in beacons1]))
    # print([item for item in beacons2 if item in beacons1])
    # print(len([1 for item in beacons1 if item not in beacons2]))

    count = 0

    for i, (_, beacons1) in enumerate(scanners[:]):
        beacons1 = parse_beacons(beacons1)

        for j, (_, beacons2) in enumerate(scanners[(i+1):]):
            beacons2 = parse_beacons(beacons2)
            print([item for item in beacons2 if item in beacons1])
            count += sum(1 for item in beacons2 if item in beacons1)

    # print(scanners[-1])
    print(count)
    return sum([len(scanner[1]) for scanner in scanners]) - count
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
