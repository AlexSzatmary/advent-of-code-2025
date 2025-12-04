import sys
import timeit


def parse(lines: list[str]) -> list[tuple[int, int]]:
    # just 1 line:
    return [
        (int(rng.split("-")[0]), int(rng.split("-")[1]))
        for rng in lines[0][:-1].split(",")
    ]  # type: ignore


def is_invalid(num: str) -> bool:
    if (length := len(num)) % 2 != 0:
        return False
    else:
        return num[: length // 2] == num[length // 2 :]


def solve_1(rngs: list[tuple[int, int]]) -> int:
    return sum(
        item for lo, hi in rngs for item in range(lo, hi + 1) if is_invalid(str(item))
    )


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
    #     print(solve_2(rotations))

    stop = timeit.default_timer()
    if "time" in argv:
        print("Time:", stop - start)


if __name__ == "__main__":
    sys.exit(main())
