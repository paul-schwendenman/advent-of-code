import fileinput




def part1(lines):

    count = 0

    for line in lines:
        [input, output] = line.strip().split(' | ')
        values = output.strip().split()

        count += sum(1 for value in values if len(value) in (2,3,4,7))

    return count


def part2(lines):

    total = 0


    for line in lines:
        one = None
        seven = None
        four = None
        eight = None
        nine_six_zero = []
        five_two_three = []

        [inputs, outputs] = line.strip().split(' | ')
        input_values = [set(item) for item in inputs.strip().split()]
        output_values = [set(item) for item in outputs.strip().split()]

        for value in output_values + input_values:
            if len(value) == 2:
                one = value
            if len(value) == 3:
                seven = value
            if len(value) == 4:
                four = value
            if len(value) == 7:
                eight = value
            if len(value) == 6:
                if value not in nine_six_zero:
                    nine_six_zero.append(value)
            if len(value) == 5:
                if value not in five_two_three:
                    five_two_three.append(value)

        assert len(five_two_three) == 3
        assert len(nine_six_zero) == 3

        a = seven - one
        three = [option for option in five_two_three if one.issubset(option)][0]
        g = three - four - a
        nine = [option for option in nine_six_zero if three | four == option][0]
        e = eight - nine
        two = [option for option in five_two_three if e.issubset(option)][0]
        five = [option for option in five_two_three if option not in (two, three)][0]
        d = (two & five) - a - g
        zero = [option for option in nine_six_zero if not d.issubset(option)][0]
        six = [option for option in nine_six_zero if option not in (zero, nine)][0]
        c = eight - six
        f = one - c
        b = four - one - d

        assert one == c | f
        assert two == a | c | d | e | g
        assert three == a | c | d | f | g
        assert four == b | d | c | f
        assert five == a | b | d| f | g
        assert six == a | b | d | e | f | g
        assert seven == a | c | f
        assert eight == a | b | c | d | e | f | g
        assert nine == a | b | c | d | f | g
        assert zero == a | b | c | e | f | g

        output = []

        for value in output_values:
            if value == zero:
                output.append('0')
            elif value == one:
                output.append('1')
            elif value == two:
                output.append('2')
            elif value == three:
                output.append('3')
            elif value == four:
                output.append('4')
            elif value == five:
                output.append('5')
            elif value == six:
                output.append('6')
            elif value == seven:
                output.append('7')
            elif value == eight:
                output.append('8')
            elif value == nine:
                output.append('9')

        total += int(''.join(output))

    return total


def main():
    with fileinput.input() as input:
        # lines = [int(value) for value in list(input)[0].split(",")]
        lines = [value for value in input]

    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
