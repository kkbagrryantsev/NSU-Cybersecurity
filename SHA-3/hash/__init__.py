__version__ = '1.1.0'
__all__ = ["sha3"]

from typing import AnyStr

from .sha3 import SHA3, SHA3Option


def sha3(data: AnyStr) -> str:
    return SHA3.hash(data, function=SHA3Option.SHA3_256)
