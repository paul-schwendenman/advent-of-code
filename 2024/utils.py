from collections.abc import Iterable
from math import log10


def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


def concat_ints(x, y):
    return x * (10 ** (int(log10(y)) + 1)) + y  # int(str(x) + str(y))
