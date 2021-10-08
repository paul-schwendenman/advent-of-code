import fileinput

def part1(strings):
    code_count = 0
    char_count = 0

    for string in strings:
        code_count += len(string.rstrip())
        char_count += len(eval(string))

        pass

    print(f"{code_count} - {char_count}")
    return code_count - char_count


def main():
    print(part1(fileinput.input()))


if __name__ == '__main__':
    main()