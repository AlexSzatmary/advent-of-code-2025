import sys
import timeit


def parse(lines: list[str]) -> list[list[int]]:
    return [list(map(int, line[:-1])) for line in lines]


def maximize_joltage(battery: list[int], n: int) -> int:
    i = -1
    result = 0
    for k in range(n):
        if k < n - 1:
            i = i + 1 + battery[i + 1:].index(max(battery[i + 1 : -(n - 1 - k)]))
        else:
            i = i + 1 + battery[i + 1:].index(max(battery[i + 1 :]))
        result = result * 10 + battery[i]
    return result


def maximize_joltage_2(battery: list[int]) -> int:
    return maximize_joltage(battery, 2)


def solve_1(batteries: list[list[int]]) -> int:
    return sum(maximize_joltage_2(battery) for battery in batteries)


def solve_2(batteries: list[list[int]]) -> int:
    return sum(maximize_joltage(battery, 12) for battery in batteries)


def main(argv: list[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv
    if argv[0] == "python":
        argv = argv[1:]
    with open(argv[-1]) as hin:
        input_lines = hin.readlines()
    batteries = parse(input_lines)
    start = timeit.default_timer()
    if "1" in argv:
        print(solve_1(batteries))
    if "2" in argv:
        print(solve_2(batteries))

    stop = timeit.default_timer()
    if "time" in argv:
        print("Time:", stop - start)


if __name__ == "__main__":
    sys.exit(main())
