from intcode import IntCode, open_program


def make_computer(program, index):
    computer =  IntCode(program[:], default_memory=8000)
    computer.add_input(index)
    return computer


def part1():
    program = open_program('input')

    computers = [make_computer(program, count) for count in range(50)]
    y_value = None

    while not y_value:
        for computer in computers:
            if not computer._inputs:
                computer._inputs.append(-1)

            computer.run()

            while computer._outputs:
                address = computer.get_output()
                x = computer.get_output()
                y = computer.get_output()

                if address == 255:
                    y_value = y
                    break
                else:
                    computers[address].add_input(x)
                    computers[address].add_input(y)
    return y_value


def main():
    program = open_program('input')

    computers = [make_computer(program, count) for count in range(50)]
    naty = None
    natx = None
    last_y = None

    while True:
        idle = True
        for computer in computers:
            if not computer._inputs:
                computer._inputs.append(-1)
            else:
                idle = False

            computer.run()

            while computer._outputs:
                address = computer.get_output()
                x = computer.get_output()
                y = computer.get_output()

                if address == 255:
                    natx = x
                    naty = y
                else:
                    computers[address].add_input(x)
                    computers[address].add_input(y)

        if idle and natx and naty:
            if last_y == naty:
                break

            computers[0].add_input(natx)
            computers[0].add_input(naty)
            last_y = naty

    return last_y


if __name__ == "__main__":
    print(main())
