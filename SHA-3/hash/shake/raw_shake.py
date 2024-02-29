from math import ceil
from collections.abc import Callable
from bitarray import bitarray
from bitarray.util import ba2hex
from hash.core.keccak import Keccak
from typing import Literal, AnyStr
from enum import Enum, auto

class RawShakeOption(Enum):
    RAW_SHAKE128 = auto()
    RAW_SHAKE256 = auto()

class RawSHAKE:
    @staticmethod
    def hash(data: AnyStr, output_length: int, function: RawShakeOption = RawShakeOption.RAW_SHAKE128) -> str:
        keccak = RawSHAKE._get_Keccak_instance(function)
        J = SHAKE._bytes2b(data)
        J.extend('11')
        hash = keccak(J, output_length)
        hash.reverse()
        hash.bytereverse()
        return RawSHAKE._b2h(hash)[::-1]

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
    def _get_Keccak_instance(function: RawShakeOption) -> Callable[[bitarray, int], bitarray]:
        match function:
            case RawShakeOption.RAW_SHAKE128:
                return Keccak(256)

            case RawShakeOption.RAW_SHAKE256:
                return Keccak(512)

            case _:
                raise ValueError("No matching hashing function found")