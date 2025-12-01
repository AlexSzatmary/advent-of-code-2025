import timeit
import sys

import numpy as np


def parse(lines: list[str]) -> np.ndarray:
    """
    Given input, creates array of rotations

    Parameters
    ----------
    lines : text of input file as list of strings

    Returns
    -------
    rotations : np.ndarray of rotations with L positive and R negative
    """
    return np.array(
        [int(("-" if line[0] == "R" else "") + line[1:-1]) for line in lines]
    )


def solve_1(rotations: np.ndarray) -> int:
    return np.sum(np.cumsum(rotations) % 100 == 50)


def main(argv: list[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv
    if argv[0] == "python":
        argv = argv[1:]
    with open(argv[-1]) as hin:
        input_lines = hin.readlines()
    rotations = parse(input_lines)
    start = timeit.default_timer()
    if "1" in argv:
        print(solve_1(rotations))
    # if "2" in argv:
    #     print(solve_2(wires, gates))

    stop = timeit.default_timer()
    if "time" in argv:
        print("Time:", stop - start)


if __name__ == "__main__":
    sys.exit(main())
