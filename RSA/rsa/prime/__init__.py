__all__ = ['is_prime']

from importlib.resources import files, as_file
from itertools import takewhile, islice
from json import load
from secrets import randbelow
from typing import Generator

import rsa.prime.resources

files = files(resources)
RABIN_MILLER_TRIALS: int = 50


def is_prime(a: int) -> bool:
    if a % 2 == 0:
        return False
    if any((a % prime == 0 for prime in takewhile(lambda prime: prime ** 2 <= a, PRIMES))):
        return False
    if not rabin_miller_test(a):
        return False
    return True


def randint_generator(low: int, high: int) -> Generator[int, None, None]:
    while True:
        yield randbelow(high - low) + low


def rabin_miller_test(n: int) -> bool:
    d = n - 1

    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    for a in islice(randint_generator(0, n - 1), RABIN_MILLER_TRIALS):
        if not pow(a, d, n) == 1 and not any([pow(a, 2 ** r * d, n) == n - 1 for r in range(s)]):
            return False

    return True


PRIMES: list[int]
with as_file(files / "primes.json") as file_path:
    with open(file_path) as file:
        PRIMES: list[int] = load(file)
