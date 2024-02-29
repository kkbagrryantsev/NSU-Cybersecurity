from math import ceil
from collections.abc import Callable
from bitarray import bitarray
from bitarray.util import ba2hex
from hash.core.keccak import Keccak
from typing import Literal, AnyStr
from enum import Enum, auto

class ShakeOption(Enum):
    SHAKE128 = auto()
    SHAKE256 = auto()

class SHAKE:
    @staticmethod
    def hash(data: AnyStr, output_length: int, function: ShakeOption = ShakeOption.SHAKE128) -> str:
        keccak = SHAKE._get_Keccak_instance(function)
        M = SHAKE._bytes2b(data)
        M.extend('1111')
        hash = keccak(M, output_length)
        hash.reverse()
        hash.bytereverse()
        return SHAKE._b2h(hash)[::-1]

    @staticmethod
    def _bytes2b(data: AnyStr) -> bitarray:
        data = bytes(data)
        msg = bitarray(endian='little')
        msg.frombytes(data)
        return msg

    @staticmethod
    def _b2h(S: bitarray) -> str:
        n = len(S)
        T = S
        T.extend('0' * ((-n) % 8))
        m = ceil(n / 8)
        b = [bitarray(8, endian='little') for i in range(m)]
        for i in range(m):
            for j in range(8):
                b[i][j] = T[8 * i + j]
        j = ''
        for i in range(m):
            j += ba2hex(b[i])
        return j

    @staticmethod
    def _get_Keccak_instance(function: ShakeOption) -> Callable[[bitarray, int], bitarray]:
        match function:
            case ShakeOption.SHAKE128:
                return Keccak(256)

            case ShakeOption.SHAKE256:
                return Keccak(512)

            case _:
                raise ValueError("No matching hashing function found")