import sys
from enum import Enum
import itertools


class Opcode(Enum):
    ADD = 1
    MULTIPY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF = 5
    JUMP_NOT_IF = 6
    LESS_THAN = 7
    EQUAL_TO = 8
    HALT = 99


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def parse_program(program):
    return (int(item) for item in program.split(','))


def split_instruction(instruction):
    opcode = Opcode(instruction % 100)
    instruction = list(str(instruction))
    parameter_modes = (["0"] * 5 + instruction)[-3:-6:-1]

    return opcode, parameter_modes


def lookup_value(memory, mode, position):
    try:
        if mode == '0':
            return memory[position]
        elif mode == '1':
            return position
    except IndexError:
        pass


def lookup_values(memory, parameter_modes, cursor):
    param_1 = lookup_value(memory, parameter_modes[0], cursor + 1)
    param_2 = lookup_value(memory, parameter_modes[1], cursor + 2)
    param_3 = lookup_value(memory, parameter_modes[2], cursor + 3)

    return param_1, param_2, param_3


class IntCode():
    def __init__(self, program):
        self.program = program[:]
        self.cursor = 0
        self.inputs = []
        self.outputs = []

    def run(self):

        while True:
            opcode, parameter_modes = split_instruction(self.program[self.cursor])

            params = lookup_values(self.program, parameter_modes, self.cursor)

            if opcode is Opcode.HALT:
                return True
            elif opcode is Opcode.ADD:
                self.program[params[2]] = self.program[params[0]] + self.program[params[1]]

                self.cursor += 4
            elif opcode is Opcode.MULTIPY:
                self.program[params[2]] = self.program[params[0]] * self.program[params[1]]

                self.cursor += 4
            elif opcode is Opcode.INPUT:
                if self.inputs:
                    self.program[params[0]] = self.inputs.pop(0)
                else:
                    return False

                self.cursor += 2
            elif opcode is Opcode.OUTPUT:
                self.outputs.append(self.program[params[0]])

                self.cursor += 2
            elif opcode is Opcode.JUMP_IF:
                if self.program[params[0]]:
                    self.cursor = self.program[params[1]]
                else:
                    self.cursor += 3
            elif opcode is Opcode.JUMP_NOT_IF:
                if not self.program[params[0]]:
                    self.cursor = self.program[params[1]]
                else:
                    self.cursor += 3
            elif opcode is Opcode.LESS_THAN:
                self.program[params[2]] = 1 if self.program[params[0]] < self.program[params[1]] else 0

                self.cursor += 4
            elif opcode is Opcode.EQUAL_TO:
                self.program[params[2]] = 1 if self.program[params[0]] == self.program[params[1]] else 0

                self.cursor += 4
            else:
                print(f"missing opcode: {opcode}")


def make_amps(program, phases):
    amps = [IntCode(program) for _ in range(5)]

    for counter in range(5):
        amps[counter].inputs.append(phases[counter])

    return amps


def run_amps(amps, amp_input):
    halted = False
    while not halted:
        for amp in amps:
            amp.inputs.append(amp_input)
            halted = amp.run()
            amp_input = amp.outputs.pop(0)

    return amp_input


def run_program(program, phases):
    best_score = 0
    for seq in itertools.permutations(phases):
        amps = make_amps(program, seq)
        output = run_amps(amps, 0)
        if output > best_score:
            best_score = output
    return best_score


def main(phases, filename='input'):
    with open(filename) as file_input:
        program_string = file_input.readlines()[0]

    program = list(parse_program(program_string))
    return run_program(program, phases)


if __name__ == "__main__":
    print(main([0, 1, 2, 3, 4]))
    print(main([5, 6, 7, 8, 9]))
