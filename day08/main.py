from typing import List
import re
import math


def part_one(puzzle_input: List[str]) -> None:
    read_nodes = {"L": " = \(([A-Z]{3}), ", "R": ", ([A-Z]{3})\)$"}
    directions = get_directions(puzzle_input)
    target_node = "AAA"
    num_steps = 0
    while target_node != "ZZZ":
        idx = (len(directions) + num_steps) % len(directions)
        d = directions[idx]
        line = get_line(target_node, puzzle_input)
        target_node = re.search(read_nodes[d], line).group(1)
        num_steps += 1
    return num_steps


def part_two(puzzle_input: List[str]) -> None:
    read_nodes = {"L": " = \(([A-Z]{3}), ", "R": ", ([A-Z]{3})\)$"}
    directions = get_directions(puzzle_input)
    r = re.compile("^[A-Z]{2}A")
    target_nodes = [
        re.search(read_nodes[directions[0]], line).group(1)
        for line in list(filter(r.match, puzzle_input))
    ]
    num_steps = []
    for target_node in target_nodes:
        n = 1
        while not re.compile("^[A-Z]{2}Z").match(target_node):
            idx = (len(directions) + n) % len(directions)
            d = directions[idx]
            line = get_line(target_node, puzzle_input)
            target_node = re.search(read_nodes[d], line).group(1)
            n += 1
        num_steps.append(n)
    return math.lcm(*num_steps)


def get_directions(puzzle_input: List[str]) -> List[str]:
    return puzzle_input[0]


def get_line(target_node: str, puzzle_input: List[str]) -> str:
    r = re.compile(f"^{target_node}")
    return list(filter(r.match, puzzle_input))[0]


def read_input_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line.rstrip() for line in f]


if __name__ == "__main__":
    test_input = read_input_file("test_input.txt")
    puzzle_input = read_input_file("input.txt")
    print(part_one(puzzle_input))
    print(part_two(test_input))
    print(part_two(puzzle_input))
