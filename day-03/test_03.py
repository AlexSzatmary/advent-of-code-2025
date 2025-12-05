import os

import pytest
from run_03 import parse, maximize_joltage, solve_1


def load(file_name: str) -> list[str]:
    inex_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(inex_path) as hin:
        lines = hin.readlines()
    return lines


@pytest.fixture
def batteries_1() -> list[list[int]]:
    return parse(load("inex-03-1.txt"))


def test_parse(batteries_1: list[list[int]]) -> None:
    assert len(batteries_1) == 4
    assert batteries_1[-1] == list(map(int, "818181911112111"))


def test_maximize_joltage(batteries_1: list[list[int]]) -> None:
    references = [98, 89, 78, 92]
    for battery, ref in zip(batteries_1, references, strict=False):
        assert maximize_joltage(battery) == ref


def test_solve_1(batteries_1: list[list[int]]) -> None:
    assert solve_1(batteries_1) == 357
