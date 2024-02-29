__all__ = ["Kuznyechik"]

from kuznyechik.constants import C, PI, PI_INV, LINEAR_TRANSFORMATION_VECTOR, GALOIS_FIELD_MULTIPLICATION_TABLE


class Kuznyechik:
    _keys: list[bytes]

    def __init__(self, key: bytes):
        self._keys = []
        _k_1 = key[:16]
        _k_2 = key[16:]
        self._keys += [_k_1, _k_2]
        for i in range(4):
            for j in range(8):
                _k_1, _k_2 = self._F(C[8 * i + j], _k_1, _k_2)
            self._keys += [_k_1, _k_2]

    @staticmethod
    def _xor(a: bytes, b: bytes) -> bytes:
        return bytes([a_i ^ b_i for a_i, b_i in zip(a, b)])

    @staticmethod
    def _l(a: bytes) -> bytes:
        result = 0
        for a_i, c_i in zip(a, LINEAR_TRANSFORMATION_VECTOR):
            result ^= GALOIS_FIELD_MULTIPLICATION_TABLE[a_i][c_i]
        return bytes([result])

    @staticmethod
    def _X(k: bytes, a: bytes) -> bytes:
        return bytes(Kuznyechik._xor(k, a))

    @staticmethod
    def _S(a: bytes) -> bytes:
        return bytes([PI[byte] for byte in a])

    @staticmethod
    def _S_inv(a: bytes) -> bytes:
        return bytes([PI_INV[byte] for byte in a])

    @staticmethod
    def _R(a: bytes) -> bytes:
        return Kuznyechik._l(a) + a[:-1]

    @staticmethod
    def _L(a: bytes) -> bytes:
        for _ in range(16):
            a = Kuznyechik._R(a)
        return a

    @staticmethod
    def _R_inv(a: bytes) -> bytes:
        return a[1:] + Kuznyechik._l(a[1:] + bytes([a[0]]))

    @staticmethod
    def _L_inv(a: bytes) -> bytes:
        for _ in range(16):
            a = Kuznyechik._R_inv(a)
        return a

    @staticmethod
    def _F(k: bytes, a1: bytes, a0: bytes) -> [bytes, bytes]:
        return Kuznyechik._xor(Kuznyechik._L(Kuznyechik._S(Kuznyechik._X(k, a1))), a0), a1

    def _E(self, a: bytes) -> bytes:
        for k_i in self._keys[:-1]:
            a = Kuznyechik._L(Kuznyechik._S(Kuznyechik._X(k_i, a)))
        a = Kuznyechik._X(self._keys[-1], a)
        return a

    def _D(self, a: bytes) -> bytes:
        for k_i in reversed(self._keys[1:]):
            a = Kuznyechik._S_inv(Kuznyechik._L_inv(Kuznyechik._X(k_i, a)))
        a = Kuznyechik._X(self._keys[0], a)
        return a

    def encrypt(self, message: bytes) -> bytes:
        # TODO Add auxiliary padding function with 2 modes as in reference implementation
        message += b"80"
        blocks = [message[i:i + 16] for i in range(0, len(message), 16)]
        blocks[-1] = blocks[-1].ljust(16, b"\0")
        encrypted_blocks = [self._E(block) for block in blocks]
        return bytes(0).join(encrypted_blocks)

    def decrypt(self, message: bytes) -> bytes:
        blocks = [message[i:i + 16] for i in range(0, len(message), 16)]
        decrypted_blocks = [self._D(block) for block in blocks]
        return bytes(0).join(decrypted_blocks).rstrip(b"\0")[:-2]
