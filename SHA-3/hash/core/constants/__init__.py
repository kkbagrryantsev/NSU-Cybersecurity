__all__ = ["RC", "ROTATION_MATRIX"]

import json
from csv import reader
from importlib.resources import as_file, files

import numpy as np
from bitarray import bitarray
from bitarray.util import hex2ba
from hash.core.constants import resources

files = files(resources)

RC: list[bitarray]
with as_file(files / "rc.json") as file_path:
    with open(file_path) as file:
        RC = [hex2ba(rc, endian="little") for rc in json.load(file)]
        assert len(RC) == 24, f"RC constant is corrupted, {len(RC) = }, while it should be 24"

ROTATION_MATRIX: list[list[int]]
with as_file(files / "rotation_matrix.csv") as file_path:
    with open(file_path) as file:
        reader = reader(file, delimiter=',')
        ROTATION_MATRIX = [[int(cell) for cell in row] for row in reader]
        shape = np.array(ROTATION_MATRIX).shape
        assert shape == (5, 5), f"ROTATION MATRIX is corrupted, {shape = }, while it should be (5, 5)]"
