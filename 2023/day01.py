import fileinput
import re

def part1(data):
    acc = 0
    for line in data:
        print(line)
        chars = [c for c in line if c in '0123456789']
        print(chars)
        acc += int(chars[0]) * 10 + int(chars[-1])

    return acc

def string_swap(line):
    line = line.replace('one', '1')
    line = line.replace('two', '2')
    line = line.replace('three', '3')
    line = line.replace('four', '4')
    line = line.replace('five', '5')
    line = line.replace('six', '6')
    line = line.replace('seven', '7')
    line = line.replace('eight', '8')
    line = line.replace('nine', '9')

    return line

def part2(data):
    acc = 0
    for line in data:
        print(line)
        # re.split('[0-9]', line)
        first = re.match(r'^.*?(one|two|three|four|five|six|seven|eight|nine|[1-9]).*', line).groups()[0]
        last = re.match(r'.*(one|two|three|four|five|six|seven|eight|nine|[1-9]).*?$', line).groups()[0]

        first = string_swap(first)
        last = string_swap(last)

        print(first, last)

        acc += int(first) * 10 + int(last)

    return acc

def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
