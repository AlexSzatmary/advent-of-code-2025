import sys
import timeit


def parse(lines: list[str]) -> list[list[int]]:
    return [list(map(int, line[:-1])) for line in lines]


def maximize_joltage(battery: list[int]) -> int:
    i1 = battery.index(max(battery[:-1]))
    i2 = battery.index(max(battery[i1 + 1:]))
    return battery[i1] * 10 + battery[i2]


def solve_1(batteries: list[list[int]]) -> int:
    return sum(maximize_joltage(battery) for battery in batteries)


def main(argv: list[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv
    if argv[0] == "python":
        argv = argv[1:]
    with open(argv[-1]) as hin:
        input_lines = hin.readlines()
    nums = parse(input_lines)
    start = timeit.default_timer()
    if "1" in argv:
        print(solve_1(nums))
    # if "2" in argv:
    #     print(solve_2(nums))

    stop = timeit.default_timer()
    if "time" in argv:
        print("Time:", stop - start)


if __name__ == "__main__":
    sys.exit(main())
