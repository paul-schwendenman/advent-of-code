import re
from collections.abc import Sequence


def extract_ints(line: str) -> Sequence[int]:
    return list(map(int, re.findall(r'-?[0-9]+', line)))
