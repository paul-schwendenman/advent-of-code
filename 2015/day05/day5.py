import fileinput

def has_three_vowels(word):
    vowels = "aeiou"
    count = 0

    for letter in word:
        if letter in vowels:
            count += 1

    return count >= 3

def has_double_letter(word):
    for num, letter in enumerate(word[:-1]):
        if letter == word[num+1]:
            return True

    return False

def has_restricted_pairs(word):
    bad_substrings = ["ab", "cd", "pq", "xy"]

    return any(substring in word for substring in bad_substrings)

def is_nice_string(word):
    return has_three_vowels(word) and has_double_letter(word) and not has_restricted_pairs(word)


def part1(filename = "input"):
    count = 0
    for line in fileinput.input(filename):
        if is_nice_string(line):
            count += 1

    return count

def main():
    print(part1())


if __name__ == '__main__':
    main()