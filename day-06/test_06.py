import os

import pytest
from run_06 import parse, solve_1, transpose, parse_2


def load(file_name: str) -> list[str]:
    inex_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(inex_path) as hin:
        lines = hin.readlines()
    return lines


@pytest.fixture
def cols_ops_1() -> tuple[list[list[int]], list[str]]:
    return parse(load("inex-06-1.txt"))


@pytest.fixture
def cols_ops_2() -> tuple[list[list[int]], list[str]]:
    return parse_2(load("inex-06-1.txt"))


def test_transpose() -> None:
    assert transpose([[0, 1], [2, 3], [4, 5]]) == [[0, 2, 4], [1, 3, 5]]


def test_parse(cols_ops_1: tuple[list[list[int]], list[str]]) -> None:
    cols, ops = cols_ops_1
    assert len(cols) == 4
    assert len(cols[0]) == 3
    assert len(ops) == 4
    assert cols[-1][-1] == 314
    assert ops[-1] == "+"


def test_solve_1(cols_ops_1: tuple[list[list[int]], list[str]]) -> None:
    cols, ops = cols_ops_1
    assert solve_1(cols, ops) == 4277556


def test_parse_2(cols_ops_2: tuple[list[list[int]], list[str]]) -> None:
    cols, ops = cols_ops_2
    assert len(cols) == 4
    assert len(cols[0]) == 3
    assert len(ops) == 4
    assert cols[-1] == [623, 431, 4]
    assert ops[-1] == "+"


def test_solve_2(cols_ops_2: tuple[list[list[int]], list[str]]) -> None:
    cols, ops = cols_ops_2
    assert solve_1(cols, ops) == 3263827
