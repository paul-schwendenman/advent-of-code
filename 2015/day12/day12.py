import fileinput
import json


def adder(input):
    if isinstance(input, dict):
        return sum(adder(item) for item in input.values())
    elif isinstance(input, list):
        return sum(adder(item) for item in input)
    elif isinstance(input, int):
        return input
    elif isinstance(input, str):
        return 0
    else:
        raise TypeError(f"what is this: {input}")


def part1(json_data):
    data = json.loads(json_data)

    return adder(data)


def main():
    print(part1(next(fileinput.input())))


if __name__ == '__main__':
    main()
