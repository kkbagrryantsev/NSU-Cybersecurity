__all__ = ['SHA3', 'SHA3Option']

from collections.abc import Callable
from enum import Enum, auto
from math import ceil
from typing import AnyStr

from bitarray import bitarray
from bitarray.util import ba2hex
from hash.core.keccak import Keccak


class SHA3Option(Enum):
    SHA3_224 = auto()
    SHA3_256 = auto()
    SHA3_384 = auto()
    SHA3_512 = auto()


class SHA3:
    @staticmethod
    def hash(data: AnyStr, function: SHA3Option = SHA3Option.SHA3_256) -> str:
        output_length: int
        match function:
            case SHA3Option.SHA3_224:
                output_length = 224
            case SHA3Option.SHA3_256:
                output_length = 256
            case SHA3Option.SHA3_384:
                output_length = 384
            case SHA3Option.SHA3_512:
                output_length = 512
        keccak = SHA3._get_Keccak_instance(function)
        M = SHA3._bytes2b(data)
        M.extend('01')
        hash = keccak(M, output_length)
        hash.reverse()
        hash.bytereverse()
        return SHA3._b2h(hash)[::-1]

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
    def _get_Keccak_instance(function: SHA3Option) -> Callable[[bitarray, int], bitarray]:
        match function:
            case SHA3Option.SHA3_224:
                return Keccak(448)

            case SHA3Option.SHA3_256:
                return Keccak(512)

            case SHA3Option.SHA3_384:
                return Keccak(768)

            case SHA3Option.SHA3_512:
                return Keccak(1024)

            case _:
                raise ValueError("No matching hashing function found")
