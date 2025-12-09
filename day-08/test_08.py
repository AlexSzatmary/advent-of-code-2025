import os

import pytest
from run_08 import (
    parse,
    calculate_distances,
    form_circuits,
    sort_take_top_3_and_multiply,
    solve_1,
    Coordinate,
)


def load(file_name: str) -> list[str]:
    inex_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(inex_path) as hin:
        lines = hin.readlines()
    return lines


@pytest.fixture
def coordinates_1() -> list[Coordinate]:
    return parse(load("inex-08-1.txt"))


def test_parse(coordinates_1: list[Coordinate]) -> None:
    assert len(coordinates_1) == 20
    assert len(coordinates_1[0]) == 3
    assert coordinates_1[-1] == (425, 690, 689)


def test_calculate_distances(coordinates_1: list[Coordinate]) -> None:
    distances = calculate_distances(coordinates_1)
    _dist, xyza, xyzb = distances[0]
    assert xyza == (162, 817, 812)
    assert xyzb == (425, 690, 689)


def test_form_circuits(coordinates_1: list[Coordinate]) -> None:
    coordinates = coordinates_1
    distances = calculate_distances(coordinates_1)
    circuits = form_circuits(coordinates, distances, 10)
    assert (len([1 for _, circuit in circuits.items() if len(circuit) == 5])) == 5
    assert (len([1 for _, circuit in circuits.items() if len(circuit) == 4])) == 4
    assert (len([1 for _, circuit in circuits.items() if len(circuit) == 1])) == 7


def test_sort_take_top_3_and_multiply(coordinates_1: list[Coordinate]) -> None:
    coordinates = coordinates_1
    distances = calculate_distances(coordinates_1)
    circuits = form_circuits(coordinates, distances, 10)
    assert sort_take_top_3_and_multiply(circuits) == 40


def test_solve_1(coordinates_1: list[Coordinate]) -> None:
    assert solve_1(coordinates_1, 10) == 40
