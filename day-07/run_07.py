import sys
import timeit


def parse(lines: list[str]) -> list[str]:
    return [s[:-1] for s in lines]


def model_tachyons(manifold: list[str]) -> tuple[list[str], int]:
    last_row = list(manifold[0])
    solution = ["".join(last_row)]
    n_splits = 0
    for row in manifold[1:]:
        modeled_row = list(row)
        for i in range(len(row)):
            if modeled_row[i] == ".":
                if last_row[i] == "|" or last_row[i] == "S":
                    modeled_row[i] = "|"
            elif modeled_row[i] == "^" and (last_row[i] == "|" or last_row[i] == "S"):
                n_splits += 1
                if i > 0:
                    modeled_row[i - 1] = "|"
                if i < len(row) - 1:
                    modeled_row[i + 1] = "|"
        solution.append("".join(modeled_row))
        last_row = modeled_row
    return solution, n_splits


def solve_1(manifold: list[str]) -> int:
    return model_tachyons(manifold)[1]


def model_tachyons_2(manifold: list[str]) -> tuple[list[str], int]:
    last_row = list(manifold[0])
    solution = ["".join(last_row)]
    n_splits = 0
    last_tachyons = [1 if c == "S" else 0 for c in manifold[0]]
    tachyons = [0] * len(last_tachyons)
    for row in manifold[1:]:
        modeled_row = list(row)
        for i in range(len(row)):
            if modeled_row[i] != "^":
                if last_row[i] == "|" or last_row[i] == "S":
                    modeled_row[i] = "|"
                    tachyons[i] += last_tachyons[i]
            elif modeled_row[i] == "^" and (last_row[i] == "|" or last_row[i] == "S"):
                n_splits += 1
                if i > 0:
                    modeled_row[i - 1] = "|"
                    tachyons[i - 1] += last_tachyons[i]
                if i < len(row) - 1:
                    modeled_row[i + 1] = "|"
                    tachyons[i + 1] += last_tachyons[i]
        solution.append("".join(modeled_row))
        last_row = modeled_row
        last_tachyons = tachyons
        tachyons = [0] * len(last_tachyons)
    return solution, sum(last_tachyons)


def solve_2(manifold: list[str]) -> int:
    return model_tachyons_2(manifold)[1]


def main(argv: list[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv
    if argv[0] == "python":
        argv = argv[1:]
    with open(argv[-1]) as hin:
        input_lines = hin.readlines()
    manifold = parse(input_lines)
    start = timeit.default_timer()
    if "1" in argv:
        print(solve_1(manifold))
    if "2" in argv:
        print(solve_2(manifold))

    stop = timeit.default_timer()
    if "time" in argv:
        print("Time:", stop - start)


if __name__ == "__main__":
    sys.exit(main())
