import unittest
from importlib.resources import files, as_file

from kuznyechik import Kuznyechik
from kuznyechik.tests import resources

files = files(resources)


class KuznyechikTest(unittest.TestCase):
    def test_S(self):
        a = bytes.fromhex('ffeeddccbbaa99881122334455667700')
        model = bytes.fromhex('b66cd8887d38e8d77765aeea0c9a7efc')
        test = (Kuznyechik._S(a))
        self.assertEqual(model, test, f"S({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('b66cd8887d38e8d77765aeea0c9a7efc')
        model = bytes.fromhex('559d8dd7bd06cbfe7e7b262523280d39')
        test = (Kuznyechik._S(a))
        self.assertEqual(model, test, f"S({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('559d8dd7bd06cbfe7e7b262523280d39')
        model = bytes.fromhex('0c3322fed531e4630d80ef5c5a81c50b')
        test = (Kuznyechik._S(a))
        self.assertEqual(model, test, f"S({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('0c3322fed531e4630d80ef5c5a81c50b')
        model = bytes.fromhex('23ae65633f842d29c5df529c13f5acda')
        test = (Kuznyechik._S(a))
        self.assertEqual(model, test, f"S({a.hex()}) expected {model.hex()}, got {test.hex()}")

    def test_S_inv(self):
        a = bytes.fromhex('b66cd8887d38e8d77765aeea0c9a7efc')
        model = bytes.fromhex('ffeeddccbbaa99881122334455667700')
        test = (Kuznyechik._S_inv(a))
        self.assertEqual(model, test, f"S_inv({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('559d8dd7bd06cbfe7e7b262523280d39')
        model = bytes.fromhex('b66cd8887d38e8d77765aeea0c9a7efc')
        test = (Kuznyechik._S_inv(a))
        self.assertEqual(model, test, f"S_inv({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('0c3322fed531e4630d80ef5c5a81c50b')
        model = bytes.fromhex('559d8dd7bd06cbfe7e7b262523280d39')
        test = (Kuznyechik._S_inv(a))
        self.assertEqual(model, test, f"S_inv({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('23ae65633f842d29c5df529c13f5acda')
        model = bytes.fromhex('0c3322fed531e4630d80ef5c5a81c50b')
        test = (Kuznyechik._S_inv(a))
        self.assertEqual(model, test, f"S_inv({a.hex()}) expected {model.hex()}, got {test.hex()}")

    def test_R(self):
        a = bytes.fromhex('00000000000000000000000000000100')
        model = bytes.fromhex('94000000000000000000000000000001')
        test = (Kuznyechik._R(a))
        self.assertEqual(model, test, f"R({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('94000000000000000000000000000001')
        model = bytes.fromhex('a5940000000000000000000000000000')
        test = (Kuznyechik._R(a))
        self.assertEqual(model, test, f"R({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('a5940000000000000000000000000000')
        model = bytes.fromhex('64a59400000000000000000000000000')
        test = (Kuznyechik._R(a))
        self.assertEqual(model, test, f"R({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('64a59400000000000000000000000000')
        model = bytes.fromhex('0d64a594000000000000000000000000')
        test = (Kuznyechik._R(a))
        self.assertEqual(model, test, f"R({a.hex()}) expected {model.hex()}, got {test.hex()}")

    def test_R_inv(self):
        a = bytes.fromhex('94000000000000000000000000000001')
        model = bytes.fromhex('00000000000000000000000000000100')
        test = (Kuznyechik._R_inv(a))
        self.assertEqual(model, test, f"R_inv({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('a5940000000000000000000000000000')
        model = bytes.fromhex('94000000000000000000000000000001')
        test = (Kuznyechik._R_inv(a))
        self.assertEqual(model, test, f"R_inv({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('64a59400000000000000000000000000')
        model = bytes.fromhex('a5940000000000000000000000000000')
        test = (Kuznyechik._R_inv(a))
        self.assertEqual(model, test, f"R_inv({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('0d64a594000000000000000000000000')
        model = bytes.fromhex('64a59400000000000000000000000000')
        test = (Kuznyechik._R_inv(a))
        self.assertEqual(model, test, f"R_inv({a.hex()}) expected {model.hex()}, got {test.hex()}")

    def test_L(self):
        a = bytes.fromhex('64a59400000000000000000000000000')
        model = bytes.fromhex('d456584dd0e3e84cc3166e4b7fa2890d')
        test = (Kuznyechik._L(a))
        self.assertEqual(model, test, f"L({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('d456584dd0e3e84cc3166e4b7fa2890d')
        model = bytes.fromhex('79d26221b87b584cd42fbc4ffea5de9a')
        test = (Kuznyechik._L(a))
        self.assertEqual(model, test, f"L({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('79d26221b87b584cd42fbc4ffea5de9a')
        model = bytes.fromhex('0e93691a0cfc60408b7b68f66b513c13')
        test = (Kuznyechik._L(a))
        self.assertEqual(model, test, f"L({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('0e93691a0cfc60408b7b68f66b513c13')
        model = bytes.fromhex('e6a8094fee0aa204fd97bcb0b44b8580')
        test = (Kuznyechik._L(a))
        self.assertEqual(model, test, f"L({a.hex()}) expected {model.hex()}, got {test.hex()}")

    def test_L_inv(self):
        a = bytes.fromhex('d456584dd0e3e84cc3166e4b7fa2890d')
        model = bytes.fromhex('64a59400000000000000000000000000')
        test = (Kuznyechik._L_inv(a))
        self.assertEqual(model, test, f"L_inv({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('79d26221b87b584cd42fbc4ffea5de9a')
        model = bytes.fromhex('d456584dd0e3e84cc3166e4b7fa2890d')
        test = (Kuznyechik._L_inv(a))
        self.assertEqual(model, test, f"L_inv({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('0e93691a0cfc60408b7b68f66b513c13')
        model = bytes.fromhex('79d26221b87b584cd42fbc4ffea5de9a')
        test = (Kuznyechik._L_inv(a))
        self.assertEqual(model, test, f"L_inv({a.hex()}) expected {model.hex()}, got {test.hex()}")

        a = bytes.fromhex('e6a8094fee0aa204fd97bcb0b44b8580')
        model = bytes.fromhex('0e93691a0cfc60408b7b68f66b513c13')
        test = (Kuznyechik._L_inv(a))
        self.assertEqual(model, test, f"L_inv({a.hex()}) expected {model.hex()}, got {test.hex()}")

    def test_key_scheduling(self):
        key = bytes.fromhex('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef')
        encryptor = Kuznyechik(key)

        hex_keys = ['8899aabbccddeeff0011223344556677', 'fedcba98765432100123456789abcdef',
                    'db31485315694343228d6aef8cc78c44', '3d4553d8e9cfec6815ebadc40a9ffd04',
                    '57646468c44a5e28d3e59246f429f1ac', 'bd079435165c6432b532e82834da581b',
                    '51e640757e8745de705727265a0098b1', '5a7925017b9fdd3ed72a91a22286f984',
                    'bb44e25378c73123a5f32f73cdb6e517', '72e9dd7416bcf45b755dbaa88e4a4043']
        model_keys = [bytes.fromhex(k_i) for k_i in hex_keys]

        self.assertListEqual(encryptor._keys, model_keys, f"Got incorrect key constants")

    def test_complex_encryption_decryption(self):
        key = bytes.fromhex('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef')
        with as_file(files.joinpath("complex.txt")) as file_path:
            with open(file_path, "rb") as file:
                data = file.read()
        encryptor = Kuznyechik(key)
        encrypted_data = encryptor.encrypt(data)
        _ = encryptor.encrypt(b"")
        decrypted_data = encryptor.decrypt(encrypted_data)
        self.assertEqual(data, decrypted_data)

    def test_filedata_encryption_decryption(self):
        key = bytes.fromhex('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef')
        encryptor = Kuznyechik(key)

        with as_file(files.joinpath("simple.txt")) as file_path:
            with open(file_path, "rb") as file:
                model_data = file.read()

        encrypted_data = encryptor.encrypt(model_data)

        with as_file(files.joinpath("encrypted_simple.txt")) as file_path:
            with open(file_path, "wb") as file:
                file.write(encrypted_data)

        with as_file(files.joinpath("encrypted_simple.txt")) as file_path:
            with open(file_path, "rb") as file:
                data = file.read()

        decrypted_data = encryptor.decrypt(data)

        with as_file(files.joinpath("decrypted_simple.txt")) as file_path:
            with open(file_path, "wb") as file:
                file.write(decrypted_data)

        with as_file(files.joinpath("decrypted_simple.txt")) as file_path:
            with open(file_path, "rb") as file:
                test_data = file.read()

        self.assertEqual(model_data, test_data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
