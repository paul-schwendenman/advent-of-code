import re
from collections.abc import *
from collections import *
from functools import *
from itertools import *
from math import inf, prod
from enum import Enum
from dataclasses import dataclass, field


def extract_ints(line):
    return list(map(int, re.findall(r'-?[0-9]+', line)))
# def extract_ints(line: str) -> Sequence[int]:
#     return list(map(int, re.findall(r'-?[0-9]+', line)))


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])



def calc_manhatten_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
