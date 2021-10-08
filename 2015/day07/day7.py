import fileinput
import re
from collections import deque

def part1(instructions):
    wires = {}

    parser = re.compile(r'(?:(?P<value>[0-9]+)|(?P<not_command>NOT )?(?P<input>[a-z]+)|(?:(?P<input_1>[a-z]+)|1) (?P<command>OR|AND|LSHIFT|RSHIFT) (?P<input_2>[a-z0-9]+)) -> (?P<output>[a-z]+)')

    instructions = deque(instructions)

    # for instruction in instructions:
    while len(instructions) > 0:
        instruction = instructions.popleft()
        if not parser.match(instruction):
            print(f'failure {instruction}')
            break

        # print(instruction)
        matches = parser.match(instruction).groupdict()
        # print(matches)
        output = matches['output']
        command = matches['command']

        if matches['value'] is not None:
            wires[output] = int(matches['value'])
        elif command is None:
            input = matches['input']

            if input not in wires:
                instructions.append(instruction)
                continue

            if matches['not_command']:
                wires[output] = 65535 - wires[input]
            else:
                wires[output] = wires[input]
        elif command == 'OR':
            input_1 = matches['input_1']
            input_2 = matches['input_2']

            if input_1 not in wires or input_2 not in wires:
                instructions.append(instruction)
                continue

            wires[output] = wires[input_1] | wires[input_2]
        elif command == 'AND':
            input_1 = matches['input_1']
            input_2 = matches['input_2']

            if input_1 is None:
                if input_2 not in wires:
                    instructions.append(instruction)
                    continue
                wires[output] = 1 & wires[input_2]
            else:
                if input_1 not in wires or input_2 not in wires:
                    instructions.append(instruction)
                    continue
                wires[output] = wires[input_1] & wires[input_2]
        elif command == 'LSHIFT':
            input_1 = matches['input_1']
            input_2 = int(matches['input_2'])

            if input_1 not in wires:
                instructions.append(instruction)
                continue

            wires[output] = wires[input_1] << input_2
        elif command == 'RSHIFT':
            input_1 = matches['input_1']
            input_2 = int(matches['input_2'])

            if input_1 not in wires:
                instructions.append(instruction)
                continue

            wires[output] = wires[input_1] >> input_2

        pass

    # print(wires)

    return wires['a']

def main():
    print(part1(fileinput.input()))
    pass


if __name__ == '__main__':
    main()
