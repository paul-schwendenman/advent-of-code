import fileinput
import itertools

class BingoCard:
    def __init__(self, board):
        self.board = board

    @classmethod
    def build(cls, raw_board):
        board = [[int(num) for num in row.split()] for row in raw_board.rstrip().split('\n')]
        return cls(board)

    @property
    def _rows(self):
        for row in self.board:
            yield row

    @property
    def _columns(self):
        for column_id in range(len(self.board[0])):
            yield [row[column_id] for row in self.board]

    @property
    def _all_nums(self) -> set:
        return set(i for row in self.board for i in row)

    def match(self, numbers):
        return any(set(group).issubset(set(numbers)) for group in itertools.chain(self._columns, self._rows))

    def score(self, numbers):
        return numbers[-1] * sum(self._all_nums.difference(numbers))

    def __str__(self):
        return ' '.join(f'{num:02}' for num in self.board[0])

def parse_board(raw_board):
    return BingoCard.build(raw_board)

def part1(lines):
    numbers = [int(num) for num in lines[0].split(',')]

    boards = [parse_board(raw_board) for raw_board in (''.join(lines[2:])).split('\n\n')]

    for i in range(len(numbers)):
        for board in boards:
            if board.match(numbers[:i]):
                break
        else:
            continue

        break

    return board.score(numbers[:i])

def part2(lines):
    numbers = [int(num) for num in lines[0].split(',')]

    boards = [parse_board(raw_board) for raw_board in (''.join(lines[2:])).split('\n\n')]

    for i in range(len(numbers)):
        for board in boards:
            if board.match(numbers[:i]):
                if len(boards) == 1:
                    break
                else:
                    boards.remove(board)
        else:
            continue

        break

    return board.score(numbers[:i])


def main():
    with fileinput.input() as input:
        lines = list(input)
    print(part1(lines))
    print(part2(lines))


if __name__ == '__main__':
    main()
