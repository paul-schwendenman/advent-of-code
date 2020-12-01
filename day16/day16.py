import itertools


def find_digit(sequence, pattern_template):
    pattern = itertools.islice(itertools.cycle(pattern_template), 1, None)

    return abs(sum(a * b for a, b in zip(sequence, pattern))) % 10


def calc_pattern(base_pattern, digit_index):
    for item in base_pattern:
        for count in range(digit_index):
            yield item


def fft(sequence, base_pattern=[0, 1, 0, -1]):
    result = []
    for count in range(len(sequence)):
        # result *= 10
        pattern = calc_pattern(base_pattern, count + 1)
        digit = find_digit(sequence, pattern)
        result.append(digit)
        # print(f'appending {digit}: {result}')

    return result


def convert_from_string(string):
    return [int(item) for item in string if item != '\n']


def convert_to_string(array):
    return "".join(str(item) for item in array)


def part1(values):
    for step in range(100):
        values = fft(values)
        print(f'step {step}: {convert_to_string(values)}')

    print(len(values))
    return convert_to_string(values)[:8]


def part2(values, offset):
    values = (values * 10000)
    for _phase in range(100):
        acc = 0

        for index in range(len(values)-1, len(values) // 2, -1):
            acc += values[index]
            values[index] = acc % 10

    return convert_to_string(values[offset:offset+8])


def main():
    with open('input') as input_file:
        data = input_file.read().rstrip()

    values = convert_from_string(data)
    offset = int(data[:7])

    # part1(values[:])
    return part2(values[:], offset)


if __name__ == "__main__":
    print(main())
