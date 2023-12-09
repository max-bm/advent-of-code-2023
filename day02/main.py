from typing import List


def part_one(puzzle_input: List[str]) -> None:
    ...


def part_two(puzzle_input: List[str]) -> None:
    ...


def read_input_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line.rstrip() for line in f]


if __name__ == "__main__":
    puzzle_input = read_input_file("input.txt")
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))
