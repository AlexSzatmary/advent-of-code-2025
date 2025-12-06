import sys
import timeit


def parse(lines: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    rngs = []
    ingredients = []
    for line in lines:
        if "-" in line:
            nums = line[:-1].split("-")
            rngs.append((int(nums[0]), int(nums[1])))
        elif line == "\n":
            pass
        else:
            ingredients.append(int(line[:-1]))

    return (rngs, ingredients)


def solve_1(rngs: list[tuple[int, int]], ingredients: list[int]) -> int:
    n = 0
    for ingredient in ingredients:
        if any(lo <= ingredient <= hi for lo, hi in rngs):
            n += 1
    return n


def main(argv: list[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv
    if argv[0] == "python":
        argv = argv[1:]
    with open(argv[-1]) as hin:
        input_lines = hin.readlines()
    rngs, ingredients = parse(input_lines)
    start = timeit.default_timer()
    if "1" in argv:
        print(solve_1(rngs, ingredients))
    # if "2" in argv:
    #     print(solve_2(rngs, ingredients))

    stop = timeit.default_timer()
    if "time" in argv:
        print("Time:", stop - start)


if __name__ == "__main__":
    sys.exit(main())
