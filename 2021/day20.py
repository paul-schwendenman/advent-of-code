import fileinput


def neighboors(pixel):
    x, y = pixel

    for j in (-1, 0, 1):
        for i in (-1, 0, 1):
            yield (x + i, y + j)


def parse_image(raw_image):
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

    min_x, max_x = min(rows), max(rows)
    min_y, max_y = min(columns), max(columns)
    padding = 2

    output = {}

    for j in range(min_y - padding, max_y + padding):
        for i in range(min_x - padding, max_x + padding):
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
