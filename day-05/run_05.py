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
    rngs, ingredients = parse(input_lines)
    start = timeit.default_timer()
    if "1" in argv:
        print(solve_1(rngs, ingredients))
    if "2" in argv:
        print(solve_2(rngs))

    stop = timeit.default_timer()
    if "time" in argv:
        print("Time:", stop - start)


if __name__ == "__main__":
    sys.exit(main())
