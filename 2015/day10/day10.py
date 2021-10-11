def look_and_say(sequence):
    output = ""
    current = sequence[0]
    count = 1

    for char in sequence[1:]:
        if char == current:
            count += 1
        else:
            output += f"{count}{current}"
            count = 1
            current = char

    output += f"{count}{current}"

    return output


def part1(sequence, repetitions=40):
    for _ in range(repetitions):
        sequence = look_and_say(sequence)

    return len(sequence)



def main():
    # print(part1("1321131112"))
    print(part1("1321131112", 50))


if __name__ == '__main__':
    main()