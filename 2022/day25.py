import fileinput


DIGITS = ((0, '0'), (1, '1'), (2, '2'), (-2, '='), (-1, '-'))


def to_snafu(number):
    digits = dict(DIGITS)

    if number == 0:
        return ''

    remainder = (number + 2) % 5 - 2
    quotient = (number + 2) // 5

    return to_snafu(quotient) + digits[remainder]


def from_snafu(number):
    digits = dict((v, k) for k, v in DIGITS)

    if not number:
        return 0

    rest, current = number[:-1], number[-1]

    return 5 * from_snafu(rest) +  digits[current]


def part1(data):
    acc = 0
    for line in data:
        acc += from_snafu(line.rstrip())

    print(acc)
    return to_snafu(acc)


def main():
    print(part1(fileinput.input()))


if __name__ == '__main__':
    main()
