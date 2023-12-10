from typing import List
import re
import math


def part_one(puzzle_input: List[str]) -> None:
    part_number_sum = 0
    for i, line in enumerate(puzzle_input):
        numbers_ind = [(int(r.group()), r.span()) for r in re.finditer(r"\d+", line)]
        a, b = max(0, i - 1), min(len(puzzle_input), i + 1)
        for n, l in numbers_ind:
            neighbourhood = "".join(get_neighbourhood(puzzle_input, (a, b), l))
            if "".join([c for c in neighbourhood if not c.isdigit() and c != "."]):
                part_number_sum += n
    return part_number_sum


def part_two(puzzle_input: List[str]) -> None:
    gear_ratio_sum = 0
    for n_line, line in enumerate(puzzle_input):
        asterisk_ind = [r.start() for r in re.finditer(r"\*+", line)]
        above, below = max(0, n_line - 1), min(len(puzzle_input) - 1, n_line + 1)
        for loc in asterisk_ind:
            master_left, master_right = loc, loc + 1
            neighbourhood = get_neighbourhood(
                puzzle_input, (above, below), (master_left, master_right)
            )
            if bool(re.search(r"\d+\D+\d+", ",".join(neighbourhood))):
                for n_reg, reg in enumerate(neighbourhood):
                    left, right = master_left, master_right
                    if any(c.isdigit() for c in reg):
                        new_left, new_right = left, right
                        while True:
                            if not (reg[0] == "." or left == 0):
                                new_left = max(0, left - 1)
                            if not (reg[-1] == "." or right == len(line)):
                                new_right = min(len(line), right + 1)
                            if new_left == left and new_right == right:
                                neighbourhood[n_reg] = reg
                                break
                            else:
                                left, right = new_left, new_right
                                reg = get_neighbourhood(
                                    puzzle_input,
                                    (above + n_reg, above + n_reg + 1),
                                    (left, right),
                                )[0]
                gear_ratio_sum += math.prod(
                    [
                        int(r.group())
                        for r in re.finditer(
                            r"\d+",
                            "".join(
                                [
                                    c
                                    for c in "".join(neighbourhood)
                                    if c.isdigit() or c == "." or c == "*"
                                ]
                            ),
                        )
                    ]
                )
    return gear_ratio_sum


def get_neighbourhood(
    input: List[str], line_numbers: tuple[int, int], line_span: tuple[int, int]
) -> str:
    return [
        line[max(0, line_span[0] - 1) : min(len(line), line_span[1] + 1)]
        for line in input[line_numbers[0] : line_numbers[1] + 1]
    ]


def read_input_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line.rstrip() for line in f]


if __name__ == "__main__":
    test_input = read_input_file("test_input.txt")
    puzzle_input = read_input_file("input.txt")
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))
