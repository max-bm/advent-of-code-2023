from typing import List


def read_input_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line.rstrip() for line in f]


def part_one(puzzle_input: List[str]) -> int:
    numbers = ["".join([c for c in line if c.isdigit()]) for line in puzzle_input]
    return sum([int(x[0] + x[-1]) for x in numbers])


def part_two(puzzle_input: List[str]) -> int:
    numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    def replace(input: str, substrings: List[str]) -> int:
        substring_locs = [
            (i, x)
            for i, x in enumerate(map(lambda x: input.find(x), substrings))
            if x != -1
        ]
        if not substring_locs:
            return input
        number = min(substring_locs, key=lambda t: t[1])[0]
        return input.replace(substrings[number], str(number + 1))

    replace_forward, replace_backward = [], []
    for line in puzzle_input:
        replace_forward.append(
            "".join([c for c in replace(line, numbers) if c.isdigit()])
        )
        replace_backward.append(
            "".join(
                [
                    c
                    for c in replace(line[::-1], [x[::-1] for x in numbers])
                    if c.isdigit()
                ]
            )
        )
    return sum([int(x[0] + y[0]) for x, y in zip(replace_forward, replace_backward)])


if __name__ == "__main__":
    puzzle_input = read_input_file("input.txt")
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))
