import os

import pytest
from run_02 import is_invalid, parse, solve_1


def load(file_name: str) -> list[str]:
    inex_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(inex_path) as hin:
        lines = hin.readlines()
    return lines


@pytest.fixture
def nums_1() -> list[tuple[int, int]]:
    return parse(load("inex-02-1.txt"))


def test_is_invalid() -> None:
    assert is_invalid("1188511885")
    assert is_invalid("11")
    assert is_invalid("22")
    assert not is_invalid("121")


def test_solve_1(nums_1: list[tuple[int, int]]) -> None:
    assert solve_1(nums_1) == 1227775554
