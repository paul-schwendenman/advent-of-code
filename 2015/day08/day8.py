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


def part2(strings):
    code_count = 0
    encode_count = 0

    for string in strings:
        code_count += len(string.rstrip())
        encode_count += len(string.rstrip().replace('\\', '\\\\').replace('"', '\\"')) + 2
        # encode_count += 2 + code_count + string.count('/') + string.count('"')
        # new = string.rstrip().replace('\\', '\\\\').replace('"', '\\"')
        # print(f"""{string}: {new}""")
        # print(f"""{len(new)} - {len(string.rstrip())}""")

        pass

    print(f"{encode_count} - {code_count}")
    return encode_count - code_count


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()