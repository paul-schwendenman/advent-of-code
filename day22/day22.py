from collections import deque, namedtuple
from typing import Iterable, Deque, Iterator, Tuple, Optional
from enum import Enum, auto


class Operation(Enum):
    CUT = auto()
    STACK = auto()
    INCREMENT = auto()


Instruction = namedtuple('Instruction', 'operation value')


def new_stack(deck: Deque) -> Deque:
    deck.reverse()
    return deck


def cut(deck: Deque, n_cards: int) -> Deque:
    deck.rotate(-n_cards)
    return deck


def increment(deck: Deque, spaces: int) -> Deque:
    number_of_cards = len(deck)
    table = [None] * number_of_cards

    pos = 0
    while deck:
        table[pos] = deck.popleft()
        pos += spaces
        if pos > number_of_cards:
            pos = (pos % number_of_cards)

    return Deque(table)


def process_instructions(instructions: Iterable[Instruction], deck: Deque) -> Deque:
    for count, (operation, value) in enumerate(instructions):
        if operation == Operation.CUT:
            deck = cut(deck, value)
        elif operation == Operation.INCREMENT:
            deck = increment(deck, value)
        elif operation == Operation.STACK:
            deck = new_stack(deck)

    return deck


def parse_instructions(instructions: Iterable[str]) -> Iterator[Tuple[Operation, Optional[int]]]:
    for instruction in instructions:
        if instruction[:3] == "cut":
            yield Instruction(Operation.CUT, int(instruction[4:]))
        elif instruction[:20] == 'deal with increment ':
            yield Instruction(Operation.INCREMENT, int(instruction[20:]))
        elif instruction == 'deal into new stack':
            yield Instruction(Operation.STACK, None)


def part1(instructions, deck_size=10, index=None):
    deck = deque(range(deck_size))
    deck = process_instructions(instructions, deck)

    return deck.index(2019)


def part2(instructions, number_of_cards, number_of_shuffles, target_location):

    for instruction in reversed(instructions):
        if instruction:
            value_at_2020 -= int(instruction[4:])
            value_at_2020 %= number_of_cards
        elif instruction[:20] == 'deal with increment ':
            spaces = int(instruction[20:])

        elif instruction == 'deal into new stack':
            value_at_2020 = number_of_cards - value_at_2020
        else:
            raise ValueError(f"Invalid instruction: '{instruction}'")

    return value_at_2020


def main():
    with open('input') as file_input:
        instructions = list(parse_instructions(file_input.read().splitlines()))

    print(f'part 1: {part1(instructions, 10007)}')
    part2_answer = part2(instructions,
                         number_of_cards=119315717514047,
                         number_of_shuffles=101741582076661,
                         target_location=2020)
    print(f'part 2: {part2_answer}')


if __name__ == "__main__":
    main()
    # for i in (2, 3):
    #     deck = deque(range(7))
    #     print(f'{i}. {increment(deck, i)}')
