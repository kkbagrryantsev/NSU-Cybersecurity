from bitarray import bitarray

from .keccak_permutation import KeccakPermutation
from .sponge import Sponge


class Keccak:
    _c: int

    def __init__(self, c: int):
        self._c = c

    @staticmethod
    def _pad(x: int, m: int) -> bitarray:
        j = (- m - 2) % x
        P = bitarray(endian='little')
        P.extend('1')
        P.extend('0' * j)
        P.extend('1')
        return P

    @staticmethod
    def _f(S: bitarray) -> bitarray:
        f = KeccakPermutation(1600, 24)
        return f(S)

    def __call__(self, N: bitarray, d: int) -> bitarray:
        sponge = Sponge(self._f, 1600, self._pad, 1600 - self._c)
        return sponge(N, d)
