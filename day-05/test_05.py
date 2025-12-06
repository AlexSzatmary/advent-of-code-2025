import os

import pytest
from run_05 import parse, solve_1


def load(file_name: str) -> list[str]:
    inex_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(inex_path) as hin:
        lines = hin.readlines()
    return lines


@pytest.fixture
def rngs_ingredients_1() -> tuple[list[tuple[int, int]], list[int]]:
    return parse(load("inex-05-1.txt"))


def test_parse(rngs_ingredients_1: tuple[list[tuple[int, int]], list[int]]) -> None:
    rngs, ingredients = rngs_ingredients_1
    assert len(rngs) == 4
    assert len(ingredients) == 6
    assert ingredients[-1] == 32


def test_solve_1(rngs_ingredients_1: tuple[list[tuple[int, int]], list[int]]) -> None:
    rngs, ingredients = rngs_ingredients_1
    assert solve_1(rngs, ingredients) == 3
