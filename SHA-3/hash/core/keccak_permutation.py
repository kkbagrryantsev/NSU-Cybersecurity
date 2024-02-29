from math import log2
from typing import TypeAlias, Literal

from bitarray import bitarray
from hash.core.constants import RC, ROTATION_MATRIX

PossiblePermutationWidth = Literal[25, 50, 100, 200, 400, 800, 1600]

StateArray: TypeAlias = list[list[bitarray]]


class KeccakPermutation:
    _b: int
    _rounds: int
    _w: int
    _l: int

    def __init__(self, b: PossiblePermutationWidth, rounds: int):
        self._b = b
        self._rounds = rounds
        self._w = self._b // 25
        self._l = int(log2(self._w))

    def _round(self, A: StateArray, i: int) -> StateArray:
        return self._iota(self._chi(self._pi(self._rho(self._theta(A)))), i)

    def _rot(self, x: bitarray, n: int) -> bitarray:
        n = n % self._w
        return (x >> n) | (x << (self._w - n))

    def _theta(self, A: StateArray) -> StateArray:
        C = [bitarray() for _ in range(5)]
        D = [bitarray('0' * self._w, endian='little') for _ in range(5)]
        for x in range(5):
            C[x] = A[x][0] ^ A[x][1] ^ A[x][2] ^ A[x][3] ^ A[x][4]
        for x in range(5):
            for z in range(self._w):
                D[x][z] = C[(x - 1) % 5][z] ^ C[(x + 1) % 5][(z - 1) % self._w]
        for x in range(5):
            for y in range(5):
                A[x][y] ^= D[x]
        return A

    def _rho(self, A: StateArray) -> StateArray:
        x, y = 1, 0
        for t in range(24):
            A[x][y] = self._rot(A[x][y], ROTATION_MATRIX[x][y])
            x, y = y, (2 * x + 3 * y) % 5
        return A

    @staticmethod
    def _pi(A: StateArray) -> StateArray:
        _A = [[bitarray(), bitarray(), bitarray(), bitarray(), bitarray()] for _ in range(5)]
        for x in range(5):
            for y in range(5):
                _A[x][y] = A[(x + 3 * y) % 5][x]
        return _A

    @staticmethod
    def _chi(A: StateArray) -> StateArray:
        _A = [[bitarray(), bitarray(), bitarray(), bitarray(), bitarray()] for _ in range(5)]
        for x in range(5):
            for y in range(5):
                _A[x][y] = A[x][y] ^ ((~A[(x + 1) % 5][y]) & A[(x + 2) % 5][y])
        return _A

    @staticmethod
    def rc(t: int) -> int:
        if t % 255 == 0:
            return 1
        R = bitarray('10000000', endian='little')
        for i in range(1, (t % 255) + 1):
            R = bitarray('0' + R.to01(), endian='little')
            R[0] ^= R[8]
            R[4] ^= R[8]
            R[5] ^= R[8]
            R[6] ^= R[8]
            R = R[:8]
        return R[0]

    def _iota(self, A: StateArray, i: int) -> StateArray:
        _RC: bitarray
        if i >= 24:
            _RC = bitarray('0' * self._w, endian='little')
            for j in range(self._l + 1):
                _RC[(2 ** j) - 1] = self.rc(j + 7 * i)
        else:
            _RC = RC[i]
        A[0][0] ^= _RC
        return A

    def __call__(self, S: bitarray) -> bitarray:
        A = self._to_state_array(S)
        for i in range(12 + 2 * self._l - self._rounds, 12 + 2 * self._l):
            A = self._round(A, i)
        return self._to_bitarray(A)

    def _to_state_array(self, S: bitarray) -> StateArray:
        A = [[bitarray(), bitarray(), bitarray(), bitarray(), bitarray()] for _ in range(5)]
        for x in range(5):
            for y in range(5):
                A[x][y] = S[(5 * y + x) * self._w:(5 * y + x) * self._w + self._w]
        return A

    @staticmethod
    def _to_bitarray(A: StateArray) -> bitarray:
        S = bitarray(endian='little')
        for i in range(5):
            for j in range(5):
                S.extend(A[j][i])
        return S
