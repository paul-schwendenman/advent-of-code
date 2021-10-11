from collections import deque
import re

def next_password(password):
    sequence = (ord(char) - ord('a') for char in reversed(password))

    acc = deque()
    overflow = 1

    for char in sequence:
        # print("-------")
        # print(f"{char} - {overflow} - {chr(char + ord('a'))}: {''.join(chr(char + ord('a')) for char in acc)}")
        next_char = (char + overflow) % 26
        acc.appendleft(next_char)
        # print(f"{char} - {overflow} - {chr(char + ord('a'))}: {''.join(chr(char + ord('a')) for char in acc)}")
        overflow = 1 if next_char == 0 else 0
        # print(f"{char} - {overflow} - {chr(char + ord('a'))}: {''.join(chr(char + ord('a')) for char in acc)}")

    return "".join(chr(char + ord('a')) for char in acc)


def is_straight(sequence):
    return chr(ord(sequence[0]) + 1) == sequence[1] and chr(ord(sequence[0]) + 2) == sequence[2]


def has_straight(password):
    for index in range(len(password) - 2):
        if is_straight(password[index:index+3]):
            return True

    return False


def has_confusing_letters(password):
    pattern = re.compile(r"[iol]")

    return pattern.search(password) is not None


def has_two_pairs(password):
    pattern = re.compile(r"([a-z])\1[a-z]*([a-z])\2")

    return pattern.search(password) is not None


def is_valid(password):
    return not has_confusing_letters(password) and has_two_pairs(password) and has_straight(password)


def next_valid_password(password):
    next_ = next_password(password)

    while not is_valid(next_):
        print(next_)
        next_ = next_password(next_)

    return next_


def part1(password):
    return next_valid_password(password)


def main():
    print(part1("cqjxjnds"))


if __name__ == '__main__':
    main()