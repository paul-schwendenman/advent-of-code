import fileinput
import json


def adder(input, *, skip_red=False):
    if isinstance(input, dict):
        if skip_red and ("red" in input.values()):
            return 0
        return sum(adder(item, skip_red=skip_red) for item in input.values())
    elif isinstance(input, list):
        return sum(adder(item, skip_red=skip_red) for item in input)
    elif isinstance(input, int):
        return input
    elif isinstance(input, str):
        return 0
    else:
        raise TypeError(f"what is this: {input}")


def part1(json_data):
    data = json.loads(json_data)

    return adder(data)


def part2(json_data):
    data = json.loads(json_data)

    return adder(data, skip_red=True)


def main():
    json_data = next(fileinput.input())
    print(part1(json_data))
    print(part2(json_data))


if __name__ == '__main__':
    main()
