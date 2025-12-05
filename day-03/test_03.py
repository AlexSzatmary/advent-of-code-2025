import os

import pytest
from run_03 import maximize_joltage, maximize_joltage_2, parse, solve_1, solve_2


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


def test_maximize_joltage_2(batteries_1: list[list[int]]) -> None:
    references = [98, 89, 78, 92]
    for battery, ref in zip(batteries_1, references, strict=False):
        assert maximize_joltage_2(battery) == ref


def test_solve_1(batteries_1: list[list[int]]) -> None:
    assert solve_1(batteries_1) == 357


def test_maximize_joltage(batteries_1: list[list[int]]) -> None:
    references = [987654321111, 811111111119, 434234234278, 888911112111]
    for battery, ref in zip(batteries_1, references, strict=False):
        assert maximize_joltage(battery, 12) == ref


def test_solve_2(batteries_1: list[list[int]]) -> None:
    assert solve_2(batteries_1) == 3121910778619
