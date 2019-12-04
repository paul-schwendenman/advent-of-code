def parse_program(program):
    return (int(item) for item in program.split(','))


def combine(noun=1, verb=1):
    # print(f'{noun:02}{verb:02}')
    return noun * 100 + verb

def run_program(program, cursor=0):
    opcode = program[cursor]

    if opcode == 99:
        return program
    elif opcode == 1:
        program[program[cursor + 3]] = program[program[cursor + 1]] + program[program[cursor + 2]]

        return run_program(program, cursor + 4)
    elif opcode == 2:
        program[program[cursor + 3]] = program[program[cursor + 1]] * program[program[cursor + 2]]

        return run_program(program, cursor + 4)

def main():
    goal = 19690720 # goal 2
    with open('day02/input') as input:
        program_string = input.readlines()[0]

    original_program = list(parse_program(program_string))

    for noun in range(0, 99):
        for verb in range(0, 99):
            program = original_program[:]
            program[1] = noun
            program[2] = verb
            # print(program[:10])
            output = run_program(program)
            # print(program[:10])

            if output[0] == goal:
                break
        else:
            continue
        break


    return combine(noun=noun, verb=verb)

if __name__ == "__main__":
    print(main())
