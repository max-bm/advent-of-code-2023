from typing import List


def part_one(puzzle_input: List[str]) -> None:
    time = [int(x) for x in puzzle_input[0].split(":")[1].strip().split(" ") if x]
    record = [int(x) for x in puzzle_input[1].split(":")[1].strip().split(" ") if x]
    result = 1
    for t, r in zip(time, record):
        number_of_ways = 0
        for i in range(t):
            speed = i
            d = speed * (t - i)
            if d > r:
                number_of_ways += 1
        result *= number_of_ways
    return result


def part_two(puzzle_input: List[str]) -> None:
    time = int(
        "".join([x for x in puzzle_input[0].split(":")[1].strip().split(" ") if x])
    )
    record = int(
        "".join([x for x in puzzle_input[1].split(":")[1].strip().split(" ") if x])
    )
    number_of_ways = 0
    for i in range(time):
        speed = i
        d = speed * (time - i)
        if d > record:
            number_of_ways += 1
    return number_of_ways


def read_input_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line.rstrip() for line in f]


if __name__ == "__main__":
    test_input = read_input_file("test_input.txt")
    puzzle_input = read_input_file("input.txt")
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))
