import os

import numpy as np
import pytest
from run_04 import parse, solve_1, count_adjacent, solve_2
from inspect import cleandoc


def load(file_name: str) -> list[str]:
    inex_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(inex_path) as hin:
        lines = hin.readlines()
    return lines


@pytest.fixture
def rolls_1() -> np.ndarray:
    return parse(load("inex-04-1.txt"))


def test_parse(rolls_1: np.ndarray) -> None:
    assert rolls_1.shape == (10, 10)


def test_count_adjacent() -> None:
    rolls = parse(
        cleandoc(
            """
            @@..
            @@@.
            @@@.
            """
        ).split()
    )
    assert count_adjacent(rolls, 0, 0) == 3
    assert count_adjacent(rolls, 1, 1) == 7
    assert count_adjacent(rolls, 1, 2) == 4
    assert count_adjacent(rolls, 2, 1) == 5


def test_solve_1(rolls_1: np.ndarray) -> None:
    assert solve_1(rolls_1) == 13


def test_solve_2(rolls_1: np.ndarray) -> None:
    assert solve_2(rolls_1) == 43
