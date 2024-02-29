__all__ = ["PI", "PI_INV", "C", "GALOIS_FIELD_MULTIPLICATION_TABLE", "LINEAR_TRANSFORMATION_VECTOR"]

from csv import reader
from json import load
from importlib.resources import files, as_file
import kuznyechik.constants.resources as resources

files = files(resources)

with as_file(files.joinpath("pi.json")) as file_path:
    with open(file_path) as file:
        PI: [int] = load(file)

with as_file(files.joinpath("pi_inv.json")) as file_path:
    with open(file_path) as file:
        PI_INV: [int] = load(file)

with as_file(files.joinpath("c.json")) as file_path:
    with open(file_path) as file:
        hex_C: [int] = load(file)
        C: [bytes] = [bytes.fromhex(C_i) for C_i in hex_C]

with as_file(files.joinpath("gf_multiplication_table.csv")) as file_path:
    with open(file_path) as file:
        reader = reader(file, delimiter=',')
        GALOIS_FIELD_MULTIPLICATION_TABLE: [[int]] = [[int(cell) for cell in row] for row in reader]

LINEAR_TRANSFORMATION_VECTOR: [int] = [148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1]
