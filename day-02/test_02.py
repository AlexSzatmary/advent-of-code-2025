import os

import pytest
from run_02 import is_invalid, parse, solve_1, is_invalid_2, invalid_rngs, solve_2


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


def test_is_invalid_2() -> None:
    assert is_invalid_2("565656")
    assert not is_invalid_2("5650656")
    assert is_invalid_2("824824824")
    assert not is_invalid_2("8248024824")


def test_invalid_rngs(nums_1: list[tuple[int, int]]) -> None:
    expected = [
        ["11", "22"],
        ["99", "111"],
        ["999", "1010"],
        ["1188511885"],
        ["222222"],
        [],
        ["446446"],
        ["38593859"],
        ["565656"],
        ["824824824"],
        ["2121212121"],
    ]
    for (lo, hi), ref in zip(nums_1, expected, strict=False):
        assert invalid_rngs(lo, hi) == list(map(int, ref))


def test_solve_2(nums_1: list[tuple[int, int]]) -> None:
    assert solve_2(nums_1) == 4174379265
