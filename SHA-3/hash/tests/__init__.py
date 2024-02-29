import unittest
from hashlib import sha3_224, sha3_256, sha3_384, sha3_512, shake_128, shake_256
from importlib.resources import as_file, files

import resources
from hash.sha3 import SHA3, SHA3Option
from hash.shake import SHAKE, ShakeOption

files = files(resources)


class HashTest(unittest.TestCase):
    def test_sha3_224_simple_message(self):
        with as_file(files / "simple.txt") as file_path:
            with open(file_path, "rb") as file:
                msg = file.read()
        custom_hash = SHA3.hash(msg, function=SHA3Option.SHA3_224)
        model_hash = sha3_224(msg).hexdigest()
        self.assertEqual(custom_hash, model_hash)

    def test_sha3_224_complex_message(self):
        with as_file(files / "complex.txt") as file_path:
            with open(file_path, "rb") as file:
                msg = file.read()
        custom_hash = SHA3.hash(msg, function=SHA3Option.SHA3_224)
        model_hash = sha3_224(msg).hexdigest()
        self.assertEqual(custom_hash, model_hash)

    def test_sha3_256_simple_message(self):
        with as_file(files / "simple.txt") as file_path:
            with open(file_path, "rb") as file:
                msg = file.read()
        custom_hash = SHA3.hash(msg, function=SHA3Option.SHA3_256)
        model_hash = sha3_256(msg).hexdigest()
        self.assertEqual(custom_hash, model_hash)

    def test_sha3_256_complex_message(self):
        with as_file(files / "complex.txt") as file_path:
            with open(file_path, "rb") as file:
                msg = file.read()
        custom_hash = SHA3.hash(msg, function=SHA3Option.SHA3_256)
        model_hash = sha3_256(msg).hexdigest()
        print(custom_hash)
        self.assertEqual(custom_hash, model_hash)

    def test_sha3_384_simple_message(self):
        with as_file(files / "simple.txt") as file_path:
            with open(file_path, "rb") as file:
                msg = file.read()
        custom_hash = SHA3.hash(msg, function=SHA3Option.SHA3_384)
        model_hash = sha3_384(msg).hexdigest()
        self.assertEqual(custom_hash, model_hash)

    def test_sha3_384_complex_message(self):
        with as_file(files / "complex.txt") as file_path:
            with open(file_path, "rb") as file:
                msg = file.read()
        custom_hash = SHA3.hash(msg, function=SHA3Option.SHA3_384)
        model_hash = sha3_384(msg).hexdigest()
        self.assertEqual(custom_hash, model_hash)

    def test_sha3_512_simple_message(self):
        with as_file(files / "simple.txt") as file_path:
            with open(file_path, "rb") as file:
                msg = file.read()
        custom_hash = SHA3.hash(msg, function=SHA3Option.SHA3_512)
        model_hash = sha3_512(msg).hexdigest()
        self.assertEqual(custom_hash, model_hash)

    def test_sha3_512_complex_message(self):
        with as_file(files / "complex.txt") as file_path:
            with open(file_path, "rb") as file:
                msg = file.read()
        custom_hash = SHA3.hash(msg, function=SHA3Option.SHA3_512)
        model_hash = sha3_512(msg).hexdigest()
        self.assertEqual(custom_hash, model_hash)

    def test_shake128_simple_message(self):
        with as_file(files / "simple.txt") as file_path:
            with open(file_path, "rb") as file:
                msg = file.read()
        custom_hash = SHAKE.hash(msg, 1024, function=ShakeOption.SHAKE128)
        model_hash = shake_128(msg).hexdigest(128)
        self.assertEqual(custom_hash, model_hash)

    def test_shake128_complex_message(self):
        with as_file(files / "complex.txt") as file_path:
            with open(file_path, "rb") as file:
                msg = file.read()
        custom_hash = SHAKE.hash(msg, 1024, function=ShakeOption.SHAKE128)
        model_hash = shake_128(msg).hexdigest(128)
        self.assertEqual(custom_hash, model_hash)

    def test_shake256_simple_message(self):
        with as_file(files / "simple.txt") as file_path:
            with open(file_path, "rb") as file:
                msg = file.read()
        custom_hash = SHAKE.hash(msg, 1024, function=ShakeOption.SHAKE256)
        model_hash = shake_256(msg).hexdigest(128)
        self.assertEqual(custom_hash, model_hash)

    def test_shake256_complex_message(self):
        with as_file(files / "complex.txt") as file_path:
            with open(file_path, "rb") as file:
                msg = file.read()
        custom_hash = SHAKE.hash(msg, 1024, function=ShakeOption.SHAKE256)
        model_hash = shake_256(msg).hexdigest(128)
        self.assertEqual(custom_hash, model_hash)


if __name__ == '__main__':
    unittest.main()
