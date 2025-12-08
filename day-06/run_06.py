import sys
import timeit
from functools import reduce
from operator import mul


def parse(lines: list[str]) -> tuple[list[list[int]], list[str]]:
    rows = [line.split() for line in lines]
    cols = transpose([list(map(int, row)) for row in rows[:-1]])
    ops = rows[-1]
    return (cols, ops)


def parse_2(lines: list[str]) -> tuple[list[list[int]], list[str]]:
    rows = [list(line) for line in lines[:-1]]
    cols = ["".join(c) for c in transpose(rows)]
    problems = []
    problem = []
    for col in cols:
        if str.isspace(col):
            problems.append(problem)
            problem = []
        else:
            problem.append(int(col))

    ops = lines[-1].split()
    return (problems, ops)


def transpose(a: list[list]) -> list[list]:
    return [list(tup) for tup in zip(*a, strict=False)]


def apply_ops(columns: list[list[int]], ops: list[str]) -> list[int]:
    return [
        sum(col) if op == "+" else reduce(mul, col)
        for (col, op) in zip(columns, ops, strict=False)
    ]


def solve_1(columns: list[list[int]], ops: list[str]) -> int:
    return sum(apply_ops(columns, ops))


def main(argv: list[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv
    if argv[0] == "python":
        argv = argv[1:]
    with open(argv[-1]) as hin:
        input_lines = hin.readlines()
    columns, ops = parse(input_lines)
    start = timeit.default_timer()
    if "1" in argv:
        print(solve_1(columns, ops))
    if "2" in argv:
        columns, ops = parse_2(input_lines)
        print(solve_1(columns, ops))

    stop = timeit.default_timer()
    if "time" in argv:
        print("Time:", stop - start)


if __name__ == "__main__":
    sys.exit(main())
