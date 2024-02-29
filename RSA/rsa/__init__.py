__all__ = ['RSA', 'RSAKey']

from hashlib import sha3_256
from itertools import islice
from secrets import token_bytes
from typing import Generator, Tuple

from rsa.prime import is_prime


class RSAKey:
    _modulus: int
    _exponent: int

    def __init__(self, modulus: int, exponent: int):
        self._modulus = modulus
        self._exponent = exponent

    def encrypt(self, data: bytes) -> bytes:
        data = int.from_bytes(data)
        encrypted_data = pow(data, self._exponent, self._modulus)
        size_bytes = (encrypted_data.bit_length() // 8) + (0 if encrypted_data.bit_length() % 8 == 0 else 1)
        return encrypted_data.to_bytes(size_bytes)

    def decrypt(self, data: bytes) -> bytes:
        data = int.from_bytes(data)
        decrypted_data = pow(data, self._exponent, self._modulus)
        size_bytes = (decrypted_data.bit_length() // 8) + (0 if decrypted_data.bit_length() % 8 == 0 else 1)
        return decrypted_data.to_bytes(size_bytes)


class RSA:
    _PRIME_OPTIONS: [int] = [65537, 257, 17, 3]

    def __init__(self, public_key: RSAKey, private_key: RSAKey):
        self._public_key = public_key
        self._private_key = private_key

    @staticmethod
    def _generate_prime(nbytes: int) -> Generator[int, None, None]:
        while True:
            random_bytes = token_bytes(nbytes)
            potential_prime = int.from_bytes(random_bytes)

            if is_prime(potential_prime):
                yield potential_prime

    @staticmethod
    def _gcd(a: int, b: int) -> Tuple[int, int, int]:
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            (q, a), b = divmod(b, a), a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return b, x0, y0

    @staticmethod
    def generate_keys(size: int) -> Tuple[RSAKey, RSAKey]:
        size = size // 8

        while True:
            p, q = islice(RSA._generate_prime(size), 2)

            if p == q:
                continue

            # g, *_ = RSA._gcd(p - 1, q - 1)
            # lambda_n = abs(p - 1 * q - 1) // g

            n = p * q
            phi_n = (p - 1) * (q - 1)
            e = next((_prime for _prime in RSA._PRIME_OPTIONS if _prime < phi_n))
            _, x, y = RSA._gcd(phi_n, e)
            d = phi_n - abs(min(x, y))

            if (d * e) % phi_n == 1:
                return RSAKey(n, e), RSAKey(n, d)

    def encrypt(self, data: bytes) -> bytes:
        return self._public_key.encrypt(data)

    def decrypt(self, data: bytes) -> bytes:
        return self._private_key.decrypt(data)

    def sign(self, data: bytes) -> bytes:
        return self._private_key.encrypt(data)

    @staticmethod
    def verify(data: bytes, signature: bytes, public_key: RSAKey) -> bool:
        decrypted_data = public_key.decrypt(signature)

        return data == decrypted_data

    def hash_sign(self, data: bytes) -> bytes:
        data_hash = sha3_256(data).digest()
        return self.sign(data_hash)

    @staticmethod
    def hash_verify(data: bytes, signature: bytes, public_key: RSAKey) -> bool:
        data_hash = sha3_256(data).digest()
        return RSA.verify(data_hash, signature, public_key)
