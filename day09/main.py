from typing import List


def part_one(puzzle_input: List[str]) -> None:
    extrapolated_sum = 0
    for history in puzzle_input:
        step_diffs = [[int(x) for x in history.split()]]
        while not all([x == 0 for x in step_diffs[-1]]):
            step_diffs.append(get_step_diff(step_diffs[-1]))
        for i in range(len(step_diffs) - 2, -1, -1):
            step_diffs[i].append(step_diffs[i][-1] + step_diffs[i + 1][-1])
        extrapolated_sum += step_diffs[0][-1]
    return extrapolated_sum


def part_two(puzzle_input: List[str]) -> None:
    extrapolated_sum = 0
    for history in puzzle_input:
        step_diffs = [[int(x) for x in history.split()]]
        while not all([x == 0 for x in step_diffs[-1]]):
            step_diffs.append(get_step_diff(step_diffs[-1]))
        for i in range(len(step_diffs) - 2, -1, -1):
            step_diffs[i] = [step_diffs[i][0] - step_diffs[i + 1][0]] + step_diffs[i]
        extrapolated_sum += step_diffs[0][0]
    return extrapolated_sum


def get_step_diff(history: List[int]) -> List[int]:
    return [history[i] - history[i - 1] for i in range(1, len(history))]


def read_input_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line.rstrip() for line in f]


if __name__ == "__main__":
    test_input = read_input_file("test_input.txt")
    puzzle_input = read_input_file("input.txt")
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))
