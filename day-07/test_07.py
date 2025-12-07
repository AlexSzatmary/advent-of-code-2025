import os

import pytest
from run_07 import parse, model_tachyons, solve_1, solve_2


def load(file_name: str) -> list[str]:
    inex_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(inex_path) as hin:
        lines = hin.readlines()
    return lines


@pytest.fixture
def manifold_1() -> list[str]:
    return parse(load("inex-07-1.txt"))


def test_parse(manifold_1: list[str]) -> None:
    assert len(manifold_1) == 16
    assert len(manifold_1[0]) == 15
    assert manifold_1[0].find("S") == 7


def test_model_tachyons(manifold_1: list[str]) -> None:
    modeled_manifold, _n = model_tachyons(manifold_1)
    assert modeled_manifold[-1] == "|.|.|.|.|.|||.|"


def test_solve_1(manifold_1: list[str]) -> None:
    assert solve_1(manifold_1) == 21


def test_solve_2(manifold_1: list[str]) -> None:
    assert solve_2(manifold_1) == 40
