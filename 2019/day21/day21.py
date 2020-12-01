from intcode import IntCode, open_program


def string_to_ascii(command):
    return map(ord, command)


def main():
    program = open_program('input')

    computer = IntCode(program, default_memory=8000)

    # J = (~A or ~B or ~C) and D

    computer._inputs.extend(string_to_ascii('NOT A T\n'))
    computer._inputs.extend(string_to_ascii('NOT B J\n'))
    computer._inputs.extend(string_to_ascii('OR T J\n'))
    computer._inputs.extend(string_to_ascii('NOT C T\n'))
    computer._inputs.extend(string_to_ascii('OR T J\n'))
    computer._inputs.extend(string_to_ascii('AND D J\n'))
    # computer._inputs.extend(string_to_ascii('WALK\n'))

    # J = J and (D and (E | H))

    computer._inputs.extend(string_to_ascii('NOT E T\n'))
    computer._inputs.extend(string_to_ascii('NOT T T\n'))
    computer._inputs.extend(string_to_ascii('OR H T\n'))
    computer._inputs.extend(string_to_ascii('AND D T\n'))
    computer._inputs.extend(string_to_ascii('AND T J\n'))
    computer._inputs.extend(string_to_ascii('RUN\n'))

    computer.run()

    for char in computer._outputs:
        try:
            print(chr(char), end='')
        except ValueError:
            return char


if __name__ == "__main__":
    print(main())
