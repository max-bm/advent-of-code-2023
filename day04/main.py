from typing import List


def part_one(puzzle_input: List[str]) -> None:
    total_points = 0
    for game in puzzle_input:
        total_numbers = calc_total_numbers(game)
        if total_numbers > 0:
            total_points += 2 ** (total_numbers - 1)
    return total_points


def part_two(puzzle_input: List[str]) -> None:
    total_scratch_cards = 0
    puzzle_input = [[game, 1] for game in puzzle_input]
    for i, (game, n_cards) in enumerate(puzzle_input):
        total_scratch_cards += n_cards
        total_numbers = calc_total_numbers(game)
        for j in range(i + 1, i + total_numbers + 1):
            puzzle_input[j][1] += n_cards
    return total_scratch_cards


def calc_total_numbers(game: str) -> int:
    split = game.split(r": ")[1].split("|")
    winning_numbers = [int(n) for n in split[0].split(" ") if n]
    numbers = [int(n) for n in split[1].split(" ") if n]
    return sum(map(lambda x: x in winning_numbers, numbers))


def read_input_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line.rstrip() for line in f]


if __name__ == "__main__":
    test_input = read_input_file("test_input.txt")
    puzzle_input = read_input_file("input.txt")
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))
