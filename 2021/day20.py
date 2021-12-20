import fileinput
from collections import defaultdict


def print_grid(grid):
    for j in range(-10, 110):
        print("".join("#" if grid.get((i, j), 0) == 1 else '.' for i in range(-10, 110)))


def neighboors(pixel):
    x, y = pixel

    for j in (-1, 0, 1):
        for i in (-1, 0, 1):
            yield (x + i, y + j)


def part1(data):
    image_enhancement_algorithm, raw_image = data[0], data[2:]

    image = defaultdict(int)

    for j, row in enumerate(raw_image):
        for i, value in enumerate(row):
            image[(i, j)] = 1 if value == '#' else 0


    pixels = [(i, j) for j in range(-100, len(raw_image) + 100) for i in range(-100, len(raw_image[0]) + 100)]

    round_1 = {}

    for pixel in pixels:
        # if all(neighboor not in image for neighboor in neighboors(pixel)):
        #     continue
        try:
            code = int("".join(str(image[neighboor]) for neighboor in neighboors(pixel)), 2)
        except Exception as e:
            print([str(image[neighboor]) for neighboor in neighboors(pixel)])
            # code = int("".join(str(image[neighboor]) for neighboor in neighboors(pixel)), 2)
            raise e
        round_1[pixel] = 1 if image_enhancement_algorithm[code] == '#' else 0
        pass

    # print_grid(round_1)
    # print('-------------')

    output = {}

    for pixel in pixels:
        # if all(neighboor not in round_1 for neighboor in neighboors(pixel)):
        #     continue
        try:
            code = int("".join(str(round_1.get(neighboor, 1)) for neighboor in neighboors(pixel)), 2)
        except Exception as e:
            print(pixel)
            print(list(neighboors(pixel)))
            print([str(output.get(neighboor, 0)) for neighboor in neighboors(pixel)])
            # code = int("".join(str(image[neighboor]) for neighboor in neighboors(pixel)), 2)
            raise e

        output[pixel] = 1 if image_enhancement_algorithm[code] == '#' else 0

    # print_grid(output)

    return sum(1 for key, item in output.items() if item and abs(key[0] < 150) and abs(key[1]) < 150)


def part2(data):
    pass


def main():
    with fileinput.input() as input:
        data = [line.rstrip() for line in input]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
