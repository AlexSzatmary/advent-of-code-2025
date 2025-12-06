import sys
import timeit

import numpy as np


def parse(lines: list[str]) -> np.ndarray:
    return np.array(
        [[1 if c == "@" else 0 for c in list(line[:-1])] for line in lines]
    )


def count_adjacent(rolls: np.ndarray, i: int, j: int) -> int:
    n = 0
    for di, dj in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
    ]:
        i1 = i + di
        j1 = j + dj
        if (
            0 <= i1 <= rolls.shape[0] - 1
            and 0 <= j1 <= rolls.shape[1] - 1
            and rolls[i1, j1] == 1
        ):
            n += 1
    return n


def solve_1(rolls: np.ndarray) -> int:
    n = 0
    for i in range(rolls.shape[0]):
        for j in range(rolls.shape[1]):
            if rolls[i, j] and count_adjacent(rolls, i, j) < 4:
                n += 1
    return n


def solve_2(rolls: np.ndarray) -> int:
    n = 0
    to_remove = []
    first_iteration = True
    while first_iteration or to_remove:
        first_iteration = False
        for roll in to_remove:
            rolls[roll] = 0
        to_remove = []
        for i in range(rolls.shape[0]):
            for j in range(rolls.shape[1]):
                if rolls[i, j] and count_adjacent(rolls, i, j) < 4:
                    n += 1
                    to_remove.append((i, j))
    return n


def main(argv: list[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv
    if argv[0] == "python":
        argv = argv[1:]
    with open(argv[-1]) as hin:
        input_lines = hin.readlines()
    rolls = parse(input_lines)
    start = timeit.default_timer()
    if "1" in argv:
        print(solve_1(rolls))
    if "2" in argv:
        print(solve_2(rolls))

    stop = timeit.default_timer()
    if "time" in argv:
        print("Time:", stop - start)


if __name__ == "__main__":
    sys.exit(main())
