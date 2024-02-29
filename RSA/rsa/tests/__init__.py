import unittest
from importlib.resources import files, as_file

from rsa import RSA
from rsa.tests import resources

files = files(resources)


class RSATest(unittest.TestCase):
    def test_simple_encryption_decryption(self):
        with as_file(files / "simple.txt") as file_path:
            with open(file_path, "rb") as file:
                message = file.read()
        public_key, private_key = RSA.generate_keys(256)
        _rsa = RSA(public_key, private_key)
        encoded_message = _rsa.encrypt(message)
        decoded_message = _rsa.decrypt(encoded_message)

        self.assertEqual(message, decoded_message)

    def test_complex_sign_verify(self):
        with as_file(files / "complex.txt") as file_path:
            with open(file_path, "rb") as file:
                message = file.read()
        public_key, private_key = RSA.generate_keys(256)
        _rsa = RSA(public_key, private_key)
        signature = _rsa.hash_sign(message)

        self.assertTrue(RSA.hash_verify(message, signature, public_key))


if __name__ == '__main__':
    unittest.main(verbosity=2)
