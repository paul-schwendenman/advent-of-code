from intcode import open_program, IntCode
from collections import namedtuple
from typing import Iterator


Point = namedtuple('Point', 'x y')


def get_neighboors(current_location: Point):
    yield Point(current_location.x - 1, current_location.y)
    yield Point(current_location.x + 1, current_location.y)
    yield Point(current_location.x, current_location.y - 1)
    yield Point(current_location.x, current_location.y + 1)


def print_grid(outputs):
    for output in outputs:
        print(chr(output), end='')

    print('')


def convert_to_array(outputs):
    path = set()
    x = 0
    y = 0
    robot = None
    for output in outputs:
        if output == 10:
            y += 1
            x = 0
            continue
        elif output == 35:
            point = Point(x, y)
            path.add(point)
        elif output in {60, 62, 94, 118}:
            if not robot:
                robot = Point(x, y)
            else:
                raise Exception('Two robots')

        x += 1

    return path, robot


def part1(program):
    computer = IntCode(program, default_memory=8000)
    computer.run()

    outputs = list(computer._outputs)
    print(f'input len: {len(computer._inputs)}')
    print(f'output len: {len(outputs)}')
    computer._outputs.clear()

    print_grid(outputs)
    scaffold, robot = convert_to_array(outputs)

    intersections = set()
    for location in scaffold:
        if all(map(lambda x: x in scaffold, get_neighboors(location))):
            intersections.add(location)

    return sum(intersection.x * intersection.y for intersection in list(intersections))


def make_instruction(instruction: str) -> Iterator[int]:
    return map(ord, instruction)


def part2(program):
    program[0] = 2
    computer = IntCode(program, default_memory=8000)
    main_prog = make_instruction('A,B,A,B,A,C,A,C,B,C\n')
    computer._inputs.extend(main_prog)
    a_func = make_instruction('R,6,L,10,R,10,R,10\n')
    computer._inputs.extend(a_func)
    b_func = make_instruction('L,10,L,12,R,10\n')
    computer._inputs.extend(b_func)
    c_func = make_instruction('R,6,L,12,L,10\n')
    computer._inputs.extend(c_func)
    video = make_instruction('y\n')
    computer._inputs.extend(video)
    computer.run()

    outputs = list(computer._outputs)
    computer._outputs.clear()

    print_grid(outputs)
    return outputs[-1:]


def main(filename='input'):
    program = open_program(filename)
    # print(part1(program))
    return part2(program[:])


if __name__ == "__main__":
    print(main())
