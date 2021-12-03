import fileinput



def part1():
    x, y = 0, 0

    with fileinput.input() as lines:
        for line in lines:
            [command, distance] = line.split(' ')

            if command == 'forward':
                pass
                x += int(distance)
            elif command == 'up':
                y -= int(distance)
                pass
            elif command == 'down':
                y += int(distance)
                pass
            else:
                raise ValueError(command, distance)
        pass
    return x * y

def part2():
    x, y, aim = 0, 0, 0

    with fileinput.input() as lines:
        for line in lines:
            [command, distance] = line.split(' ')

            if command == 'forward':
                pass
                x += int(distance)
                y += int(distance) * aim
            elif command == 'up':
                aim -= int(distance)
                pass
            elif command == 'down':
                aim += int(distance)
                pass
            else:
                raise ValueError(command, distance)
        pass
    return x * y

def main():
    print(part1())
    print(part2())

if __name__ == '__main__':
    main()
