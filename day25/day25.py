from intcode import IntCode, open_program
from typing import Iterator
import random


def make_instruction(instruction: str) -> Iterator[int]:
    return map(ord, instruction + '\n')


if __name__ == "__main__":
    program = open_program('input')
    computer = IntCode(program, default_memory=8000)
    inputs = [
        make_instruction('west'),
        make_instruction('west'),
        make_instruction('north'),
        make_instruction('take space heater'),
        make_instruction('south'),
        make_instruction('east'),
        make_instruction('south'),
        make_instruction('take festive hat'),
        make_instruction('south'),
        make_instruction('take sand'),
        make_instruction('north'),
        make_instruction('east'),
        make_instruction('take whirled peas'),
        make_instruction('west'),
        make_instruction('north'),
        make_instruction('east'),

        make_instruction('south'),
        make_instruction('take weather machine'),
        make_instruction('north'),

        make_instruction('east'),
        make_instruction('take mug'),
        make_instruction('east'),
        make_instruction('south'),
        make_instruction('east'),
        make_instruction('south'),
        make_instruction('take easter egg'),
        make_instruction('north'),
        make_instruction('west'),
        make_instruction('west'),
        make_instruction('south'),
        make_instruction('west'),
        make_instruction('take shell'),
        make_instruction('south'),
        make_instruction('south'),
    ]
    for instruction in inputs:
        computer._inputs.extend(instruction)

    inventory = [
        'space heater',
        'festive hat',
        'sand',
        'whirled peas',
        'weather machine',
        'mug',
        'easter egg',
        'shell',
    ]
    floor = []

    while True:
        computer.run()

        output = "".join(map(chr, computer._outputs))
        computer._outputs.clear()

        print(output, end='')
        # input_command = make_instruction(input())

        if 'lighter' in output:
            item = random.choice(inventory)
            inventory.remove(item)
            floor.append(item)
            input_command = make_instruction(f'drop {item}\nsouth')
        elif 'heavier' in output:
            item = random.choice(floor)
            floor.remove(item)
            inventory.append(item)
            input_command = make_instruction(f'take {item}\nsouth')
        else:
            break
            # input_command = make_instruction(input())

        computer._inputs.extend(input_command)
