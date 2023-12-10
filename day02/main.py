from typing import List
import re
import math


def part_one(puzzle_input: List[str]) -> None:
    colours = {"red": 12, "green": 13, "blue": 14}

    def colour_bool(game: str, colour: tuple[str, int]) -> bool:
        colour_idx = [r.start() for r in re.finditer(colour[0], game)]
        return max([int(game[i - 3 : i - 1]) for i in colour_idx]) <= colour[1]

    return sum(
        [
            all([colour_bool(game, c) for c in colours.items()]) * (i + 1)
            for i, game in enumerate(puzzle_input)
        ]
    )


def part_two(puzzle_input: List[str]) -> None:
    def colour_min(game: str, colour: str) -> int:
        colour_idx = [r.start() for r in re.finditer(colour, game)]
        return max([int(game[i - 3 : i - 1]) for i in colour_idx])

    return sum(
        [
            math.prod([colour_min(game, c) for c in ["red", "green", "blue"]])
            for game in puzzle_input
        ]
    )


def read_input_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line.rstrip() for line in f]


if __name__ == "__main__":
    puzzle_input = read_input_file("input.txt")
    # test_input = read_input_file("test_input.txt")
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))
