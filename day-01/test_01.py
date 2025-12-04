import os

import numpy as np
import pytest
from run_01 import parse, solve_1, solve_2


def load(file_name: str) -> list[str]:
    inex_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(inex_path) as hin:
        lines = hin.readlines()
    return lines


@pytest.fixture
def rotations_1() -> np.ndarray:
    return parse(load("inex-01-1.txt"))


def test_solve_1(rotations_1: np.ndarray) -> None:
    assert solve_1(rotations_1) == 3


def test_solve_2(rotations_1: np.ndarray) -> None:
    assert solve_2(rotations_1) == 6
