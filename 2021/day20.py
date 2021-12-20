import fileinput


def neighboors(pixel):
    x, y = pixel

    for j in (-1, 0, 1):
        for i in (-1, 0, 1):
            yield (x + i, y + j)


def parse_image(raw_image):
    # image = {}

    # for j, row in enumerate(raw_image):
    #     for i, value in enumerate(row):
    #         image[(i, j)] = 1 if value == "#" else 0

    return {
        (i, j): (1 if value == "#" else 0)
        for j, row in enumerate(raw_image)
        for i, value in enumerate(row)
    }


def process_image(image_enhancement_algorithm, pixels, step):
    rows = []
    columns = []

    for x, y in pixels:
        rows.append(y)
        columns.append(x)

    max_x = max(rows)
    min_x = min(rows)
    max_y = max(columns)
    min_y = min(columns)

    output = {}

    for j in range(min_y - 2, max_y + 2):
        for i in range(min_x - 2, max_x + 2):
            pixel = (i, j)

            code = int(
                "".join(
                    str(pixels.get(neighboor, step % 2))
                    for neighboor in neighboors(pixel)
                ),
                2,
            )

            output[pixel] = 1 if image_enhancement_algorithm[code] == "#" else 0

    return output


def part1(data, steps=2):
    image_enhancement_algorithm, raw_image = data[0], data[2:]

    image = parse_image(raw_image)

    for step in range(steps):
        image = process_image(image_enhancement_algorithm, image, step)

    return sum(1 for item in image.values() if item)


def main():
    with fileinput.input() as input:
        data = [line.rstrip() for line in input]

    print(part1(data))
    print(part1(data, 50))


if __name__ == "__main__":
    main()
