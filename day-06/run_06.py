import sys
import timeit
from functools import reduce
from operator import mul


def parse(lines: list[str]) -> tuple[list[list[int]], list[str]]:
    rows = [line.split() for line in lines]
    cols = transpose([list(map(int, row)) for row in rows[:-1]])
    ops = rows[-1]
    return (cols, ops)


def transpose(a: list[list]) -> list[list]:
    return [list(tup) for tup in zip(*a, strict=False)]


def apply_ops(columns: list[list[int]], ops: list[str]) -> list[int]:
    return [
        sum(col) if op == "+" else reduce(mul, col)
        for (col, op) in zip(columns, ops, strict=False)
    ]


def solve_1(columns: list[list[int]], ops: list[str]) -> int:
    return sum(apply_ops(columns, ops))


def merge_ranges(rngs: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged_rngs = []
    rngs = sorted(rngs)
    while rngs:
        rng1 = rngs[0]
        k = 0
        for k, rng2 in enumerate(rngs[1:]):
            if rng2[0] <= rng1[1]:
                if rng1[1] <= rng2[1]:
                    rng1 = (rng1[0], rng2[1])
            else:
                k -= 1
                break
        merged_rngs.append(rng1)
        rngs = rngs[k + 2 :]
    return merged_rngs


def solve_2(rngs: list[tuple[int, int]]) -> int:
    merged_rngs = merge_ranges(rngs)
    return sum(hi - lo + 1 for lo, hi in merged_rngs)


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
    # if "2" in argv:
    #     print(solve_2(columns, ops))

    stop = timeit.default_timer()
    if "time" in argv:
        print("Time:", stop - start)


if __name__ == "__main__":
    sys.exit(main())
