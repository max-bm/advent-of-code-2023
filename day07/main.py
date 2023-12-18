from typing import List


def part_one(puzzle_input: List[str]) -> None:
    card_rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    ranked_hands = []
    for line in puzzle_input:
        hand, bid = line.split()[0], int(line.split()[1])
        number_of_each_card = get_number_of_each_card(hand, card_rank)
        type = get_type(number_of_each_card)
        strength = get_strength(hand, card_rank)
        line = (type, *strength, bid)
        ranked_hands.append(line)
    return get_total_winnings(ranked_hands)


def part_two(puzzle_input: List[str]) -> None:
    card_rank = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    ranked_hands = []
    for line in puzzle_input:
        hand, bid = line.split()[0], int(line.split()[1])
        number_of_each_card = get_number_of_each_card_with_wildcard(hand, card_rank)
        type = get_type(number_of_each_card)
        strength = get_strength(hand, card_rank)
        line = (type, *strength, bid)
        ranked_hands.append(line)
    return get_total_winnings(ranked_hands)


def get_number_of_each_card(hand: str, card_rank: List[str]) -> List[int]:
    return [hand.count(card) for card in card_rank]


def get_number_of_each_card_with_wildcard(hand: str, card_rank: List[str]) -> List[int]:
    number_of_each_card = get_number_of_each_card(hand, card_rank)
    index_max = max(
        range(len(number_of_each_card[:-1])), key=number_of_each_card[:-1].__getitem__
    )
    number_of_each_card[index_max] += number_of_each_card[-1]
    return number_of_each_card[:-1]


def get_type(number_of_each_card: List[int]) -> int:
    if max(number_of_each_card) == 5:
        return 0
    elif max(number_of_each_card) == 4:
        return 1
    elif max(number_of_each_card) == 3:
        if 2 in number_of_each_card:
            return 2
        else:
            return 3
    elif max(number_of_each_card) == 2:
        if number_of_each_card.count(2) == 2:
            return 4
        else:
            return 5
    else:
        return 6


def get_strength(hand: str, card_rank) -> str:
    return [card_rank.index(card) for card in hand]


def get_total_winnings(ranked_hands: List[tuple[int]]) -> int:
    sorted_hands = sorted(
        ranked_hands, key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]), reverse=True
    )
    total_winnings = 0
    for i, hand in enumerate(sorted_hands):
        total_winnings += hand[-1] * (i + 1)
    return total_winnings


def read_input_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line.rstrip() for line in f]


if __name__ == "__main__":
    test_input = read_input_file("test_input.txt")
    puzzle_input = read_input_file("input.txt")
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))
