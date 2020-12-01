'''Intcode Machine

An implementation of the intcode computer for Advent of Code 2019
'''
import sys
from enum import Enum
from collections import deque
from typing import Iterable, List, Tuple, Any, Optional, Deque


__author__ = 'Paul Schwendenman'
__email__ = 'schwendenman.paul+intcode@gmail.com'
__license__ = 'MIT'
__version__ = '0.1.0'


class MissingParameterMode(Exception):
    pass


class MissingOpcode(Exception):
    pass


class Opcode(Enum):
    ADD = 1
    MULTIPY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF = 5
    JUMP_NOT_IF = 6
    LESS_THAN = 7
    EQUAL_TO = 8
    ADJUST_RELATIVE_BASE = 9
    HALT = 99


class ParameterMode(Enum):
    POSITION = '0'
    IMMEDIATE = '1'
    RELATIVE = '2'


def eprint(*args: Any, **kwargs: Any) -> None:  # type: ignore
    print(*args, file=sys.stderr, **kwargs)  # type: ignore


def parse_program(program: str) -> Iterable[int]:
    return (int(item) for item in program.split(','))


def split_instruction(instruction: int) -> Tuple[Opcode, List[ParameterMode]]:
    opcode = Opcode(instruction % 100)
    deconstructed_instruction = list(str(instruction))
    parameter_modes = [ParameterMode(mode) for mode in (["0"] * 5 + deconstructed_instruction)[-3:-6:-1]]

    return opcode, parameter_modes


def lookup_value(memory: List[int], mode: ParameterMode, position: int, relative_base: int) -> int:
    if mode == ParameterMode.POSITION:
        return memory[position]
    elif mode == ParameterMode.IMMEDIATE:
        return position
    elif mode == ParameterMode.RELATIVE:
        return relative_base + memory[position]
    else:
        raise MissingParameterMode


def lookup_values(memory: List[int], parameter_modes: List[ParameterMode], cursor: int, relative_base: int) -> Tuple[int, int, int]:  # noqa: E501
    param_1 = lookup_value(memory, parameter_modes[0], cursor + 1, relative_base)
    param_2 = lookup_value(memory, parameter_modes[1], cursor + 2, relative_base)
    param_3 = lookup_value(memory, parameter_modes[2], cursor + 3, relative_base)

    return param_1, param_2, param_3


class IntCode():
    def __init__(self, program: Optional[List[int]] = None, default_memory: int = 2000, debug: bool = False):
        self._memory = [0] * default_memory
        self._cursor = 0
        self._relative_base = 0
        self._debug = debug

        if program:
            self.load_program(program)

        self._inputs: Deque[int] = deque()
        self._outputs: Deque[int] = deque()

    def load_program(self, program: List[int]) -> None:
        self._memory[:len(program)] = program

    def run(self) -> bool:
        while True:
            opcode, parameter_modes = split_instruction(self._memory[self._cursor])

            params = lookup_values(self._memory, parameter_modes, self._cursor, self._relative_base)
            if self._debug:
                eprint(f'{opcode} {params} {parameter_modes}')

            if opcode is Opcode.HALT:
                return True
            elif opcode is Opcode.ADD:
                self._memory[params[2]] = self._memory[params[0]] + self._memory[params[1]]

                self._cursor += 4
            elif opcode is Opcode.MULTIPY:
                self._memory[params[2]] = self._memory[params[0]] * self._memory[params[1]]

                self._cursor += 4
            elif opcode is Opcode.INPUT:
                if self._inputs:
                    self._memory[params[0]] = self._inputs.popleft()
                else:
                    return False

                self._cursor += 2
            elif opcode is Opcode.OUTPUT:
                self._outputs.append(self._memory[params[0]])

                self._cursor += 2
            elif opcode is Opcode.JUMP_IF:
                if self._memory[params[0]]:
                    self._cursor = self._memory[params[1]]
                else:
                    self._cursor += 3
            elif opcode is Opcode.JUMP_NOT_IF:
                if not self._memory[params[0]]:
                    self._cursor = self._memory[params[1]]
                else:
                    self._cursor += 3
            elif opcode is Opcode.LESS_THAN:
                self._memory[params[2]] = 1 if self._memory[params[0]] < self._memory[params[1]] else 0

                self._cursor += 4
            elif opcode is Opcode.EQUAL_TO:
                self._memory[params[2]] = 1 if self._memory[params[0]] == self._memory[params[1]] else 0

                self._cursor += 4
            elif opcode is Opcode.ADJUST_RELATIVE_BASE:
                self._relative_base += self._memory[params[0]]

                self._cursor += 2
            else:
                raise MissingOpcode(opcode)

    def get_output(self) -> int:
        return self._outputs.popleft()

    def has_output(self) -> bool:
        return len(self._outputs) > 0

    def add_input(self, value: int) -> None:
        self._inputs.append(value)


def open_program(filename: str) -> List[int]:
    with open(filename) as input_file:
        program = parse_program(input_file.read())

    return list(program)


__all__ = ["open_program", "parse_program", "IntCode"]
