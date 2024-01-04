from typing import List


def part_one(puzzle_input: List[str]) -> None:
    expanded_input = expand_vertical(expand_horizontal(puzzle_input))
    galaxy_locs = [
        (i, j)
        for i, row in enumerate(expanded_input)
        for j, x in enumerate(row)
        if x == "#"
    ]
    min_steps = []
    for i in range(len(galaxy_locs)):
        for j in range(i + 1, len(galaxy_locs)):
            min_steps.append(
                abs(galaxy_locs[i][0] - galaxy_locs[j][0])
                + abs(galaxy_locs[i][1] - galaxy_locs[j][1])
            )
    return sum(min_steps)


def part_two(puzzle_input: List[str]) -> None:
    expansion_rate = 999999
    empty_rows = [
        i for i, line in enumerate(puzzle_input) if all(x == "." for x in line)
    ]
    empty_cols = [
        i
        for i, line in enumerate(["".join(s) for s in zip(*puzzle_input)])
        if all(x == "." for x in line)
    ]
    galaxy_locs = [
        (i, j)
        for i, row in enumerate(puzzle_input)
        for j, x in enumerate(row)
        if x == "#"
    ]
    for i, loc in enumerate(galaxy_locs):
        r = loc[0] + expansion_rate * len([x for x in empty_rows if x < loc[0]])
        c = loc[1] + expansion_rate * len([x for x in empty_cols if x < loc[1]])
        galaxy_locs[i] = (r, c)
    min_steps = []
    for i in range(len(galaxy_locs)):
        for j in range(i + 1, len(galaxy_locs)):
            min_steps.append(
                abs(galaxy_locs[i][0] - galaxy_locs[j][0])
                + abs(galaxy_locs[i][1] - galaxy_locs[j][1])
            )
    return sum(min_steps)


def expand_vertical(puzzle_input: List[str]) -> List[str]:
    rows_to_add = []
    for i, line in enumerate(puzzle_input):
        if all(x == "." for x in line):
            rows_to_add.append(i)
    for i, r in enumerate(rows_to_add):
        puzzle_input.insert(r + i, "." * len(puzzle_input[0]))
    return puzzle_input


def expand_horizontal(puzzle_input: List[str]) -> List[str]:
    puzzle_input = ["".join(s) for s in zip(*puzzle_input)]
    expand_vertical(puzzle_input)
    return ["".join(s) for s in zip(*puzzle_input)]


def read_input_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line.rstrip() for line in f]


if __name__ == "__main__":
    test_input = read_input_file("test_input.txt")
    puzzle_input = read_input_file("input.txt")
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))
