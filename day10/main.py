from typing import List
import copy

get_next_pipe = {
    "|": lambda x, y: [(x - 1, y), (x + 1, y)],
    "-": lambda x, y: [(x, y - 1), (x, y + 1)],
    "L": lambda x, y: [(x - 1, y), (x, y + 1)],
    "J": lambda x, y: [(x - 1, y), (x, y - 1)],
    "7": lambda x, y: [(x + 1, y), (x, y - 1)],
    "F": lambda x, y: [(x + 1, y), (x, y + 1)],
}


def part_one(puzzle_input: List[str]) -> None:
    i, j = get_start(puzzle_input)
    target_pipe, _ = get_pipes_from_start(puzzle_input, i, j)
    prev_pipe = (i, j)
    step_number = 1
    while target_pipe != (i, j):
        target_pipe, prev_pipe = number_steps(
            puzzle_input, target_pipe, prev_pipe, step_number
        )
        step_number += 1
    return (
        max([int(x) for line in puzzle_input for x in line if isinstance(x, int)]) + 1
    ) // 2


def part_two(puzzle_input: List[str]) -> None:
    master_puzzle_input = copy.deepcopy(puzzle_input)
    i, j = get_start(puzzle_input)
    master_puzzle_input = replace_start_with_pipe(master_puzzle_input, i, j)
    target_pipe, _ = get_pipes_from_start(puzzle_input, i, j)
    prev_pipe = (i, j)
    step_number = 1
    while target_pipe != (i, j):
        target_pipe, prev_pipe = number_steps(
            puzzle_input, target_pipe, prev_pipe, step_number
        )
        step_number += 1
    enclosed_area = 0
    for i, line in enumerate(puzzle_input):
        count = False
        boundary = ""
        for j, x in enumerate(line):
            if isinstance(x, int) or x == "S":
                # This is always going from inside to outside, or vice versa
                if master_puzzle_input[i][j] == "|":
                    count = not count
                elif master_puzzle_input[i][j] in ["F", "L"]:
                    boundary = master_puzzle_input[i][j]
                elif master_puzzle_input[i][j] == "J" and boundary == "F":
                    count = not count
                elif master_puzzle_input[i][j] == "7" and boundary == "L":
                    count = not count
            elif count:
                enclosed_area += 1
    return enclosed_area


def get_start(puzzle_input: List[str]) -> tuple:
    return [(i, line.index("S")) for i, line in enumerate(puzzle_input) if "S" in line][
        0
    ]


def number_steps(
    puzzle_input: List[str], pipe_loc: tuple, prev_loc: tuple, step_number: int
) -> None:
    pipe_type = puzzle_input[pipe_loc[0]][pipe_loc[1]]
    puzzle_input[pipe_loc[0]][pipe_loc[1]] = step_number
    next_pipe = get_next_pipe[pipe_type](pipe_loc[0], pipe_loc[1])
    next_pipe.remove(prev_loc)
    return next_pipe[0], pipe_loc


def get_pipes_from_start(puzzle_input: List[str], i: int, j: int) -> List[str]:
    pipes = []
    if i > 0 and puzzle_input[i - 1][j] in ["|", "7", "F"]:
        pipes.append((i - 1, j))
    if i < len(puzzle_input) - 1 and puzzle_input[i + 1][j] in ["|", "J", "L"]:
        pipes.append((i + 1, j))
    if j > 0 and puzzle_input[i][j - 1] in ["-", "F", "L"]:
        pipes.append((i, j - 1))
    if j < len(puzzle_input[i]) - 1 and puzzle_input[i][j + 1] in ["-", "7", "J"]:
        pipes.append((i, j + 1))
    return pipes[0], pipes[1]


def replace_start_with_pipe(puzzle_input: List[str], i: int, j: int) -> List[str]:
    pipes = ["|", "-", "L", "J", "7", "F"]
    if i > 0 and puzzle_input[i - 1][j] in ["|", "7", "F"]:
        pipes = [p for p in pipes if p not in ["-", "7", "F"]]
    if i < len(puzzle_input) - 1 and puzzle_input[i + 1][j] in ["|", "J", "L"]:
        pipes = [p for p in pipes if p not in ["-", "J", "L"]]
    if j > 0 and puzzle_input[i][j - 1] in ["-", "F", "L"]:
        pipes = [p for p in pipes if p not in ["|", "F", "L"]]
    if j < len(puzzle_input[i]) - 1 and puzzle_input[i][j + 1] in ["-", "7", "J"]:
        pipes = [p for p in pipes if p not in ["|", "7", "J"]]
    puzzle_input[i][j] = pipes[0]
    return puzzle_input


def read_input_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [[x for x in line.rstrip()] for line in f]


if __name__ == "__main__":
    test_input = read_input_file("test_input.txt")
    test_input_2 = read_input_file("test_input_part_2.txt")
    puzzle_input_1 = read_input_file("input.txt")
    puzzle_input_2 = copy.deepcopy(puzzle_input_1)
    print(part_one(puzzle_input_1))
    print(part_two(puzzle_input_2))
