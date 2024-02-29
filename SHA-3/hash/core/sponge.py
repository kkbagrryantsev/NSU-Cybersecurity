from collections.abc import Callable

from bitarray import bitarray


class Sponge:
    _f: Callable[[bitarray], bitarray]
    _b: int
    _pad: Callable[[int, int], bitarray]
    _r: int

    def __init__(self, f: Callable[[bitarray], bitarray], b: int, pad: Callable[[int, int], bitarray], r: int):
        self._f = f
        self._b = b
        self._pad = pad
        self._r = r

    def __call__(self, N: bitarray, d: int) -> bitarray:
        P = N
        P.extend(self._pad(self._r, len(N)))
        S = self._absorb(P)
        Z = self._squeeze(S, d)
        return Z

    def _absorb(self, P: bitarray) -> bitarray:
        n = len(P) // self._r
        c = self._b - self._r
        S = bitarray('0' * self._b, endian='little')
        for i in range(n):
            Pi = P[i * self._r:i * self._r + self._r]
            Pi.extend('0' * c)
            S = self._f(S ^ Pi)
        return S

    def _squeeze(self, S: bitarray, d: int) -> bitarray:
        Z = bitarray(endian='little')
        Z.extend(S[:self._r])
        while d > len(Z):
            S = self._f(S)
            Z.extend(S[:self._r])
        return Z[:d]
