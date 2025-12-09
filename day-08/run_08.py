import sys
import timeit

Coordinate = tuple[int, int, int]


def parse(lines: list[str]) -> list[Coordinate]:
    return [
        (int(a[0]), int(a[1]), int(a[2])) for a in [s[:-1].split(",") for s in lines]
    ]


def calculate_distances(
    coordinates: list[Coordinate],
) -> list[tuple[float, Coordinate, Coordinate]]:
    """
    Actually finds distances squared, which is fine because we only use distances for
    sorting
    """
    distances = []
    for i1, xyz1 in enumerate(coordinates[:-1]):
        x1, y1, z1 = xyz1
        for xyz2 in coordinates[i1 + 1 :]:
            x2, y2, z2 = xyz2
            distances.append(
                (
                    (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2,
                    min(xyz1, xyz2),
                    max(xyz1, xyz2),
                )
            )
    distances.sort()
    return distances


def form_circuits(
    coordinates: list[Coordinate],
    distances: list[tuple[float, Coordinate, Coordinate]],
    n_connections: int,
) -> dict[Coordinate, list[Coordinate]]:
    circuits = {x: [x] for x in coordinates}
    for i in range(n_connections):
        _, a, b = distances[i]
        if b in circuits[a]:  # already connected
            continue
        merge_circuits(circuits, a, b)
    return circuits


def merge_circuits(
    circuits: dict[Coordinate, list[Coordinate]], a: Coordinate, b: Coordinate
) -> None:
    """
    Modifies circuits in place
    """
    circuits[a].extend(circuits[b])
    for c in circuits[b]:
        circuits[c] = circuits[a]


def sort_take_top_3_and_multiply(
    circuits: dict[Coordinate, list[Coordinate]],
) -> int:
    unique_circuits = [
        list(c) for c in {tuple(circuit) for circuit in circuits.values()}
    ]
    lengths = list(map(len, unique_circuits))
    lengths.sort(reverse=True)
    return lengths[0] * lengths[1] * lengths[2]


def solve_1(coordinates: list[Coordinate], n_connections: int) -> int:
    distances = calculate_distances(coordinates)
    circuits = form_circuits(coordinates, distances, n_connections)
    return sort_take_top_3_and_multiply(circuits)


def form_circuits_2(
    coordinates: list[Coordinate],
    distances: list[tuple[float, Coordinate, Coordinate]],
) -> int:
    circuits = {x: [x] for x in coordinates}
    for _, a, b in distances:
        if b in circuits[a]:  # already connected
            continue
        merge_circuits(circuits, a, b)
        if len(circuits[a]) == len(coordinates):
            return a[0] * b[0]
    return -1


def solve_2(coordinates: list[Coordinate]) -> int:
    distances = calculate_distances(coordinates)
    return form_circuits_2(coordinates, distances)


def main(argv: list[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv
    if argv[0] == "python":
        argv = argv[1:]
    with open(argv[-1]) as hin:
        input_lines = hin.readlines()
    coordinates = parse(input_lines)
    start = timeit.default_timer()
    if "1" in argv:
        print(solve_1(coordinates, 1000))
    if "2" in argv:
        print(solve_2(coordinates))

    stop = timeit.default_timer()
    if "time" in argv:
        print("Time:", stop - start)


if __name__ == "__main__":
    sys.exit(main())
