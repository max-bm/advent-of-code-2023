from typing import List
from itertools import groupby


def part_one(puzzle_input: List[str]) -> None:
    seeds = [int(s) for s in puzzle_input[0].split(": ")[1].split()]
    maps = [list(m) for k, m in groupby(puzzle_input[2:], key=bool) if k]
    locs = []
    for seed in seeds:
        for map in maps:
            seed = compute_mapping(seed, map)
        locs.append(seed)
    return min(locs)


def part_two(puzzle_input: List[str]) -> None:
    sds = [int(s) for s in puzzle_input[0].split(": ")[1].split()]
    maps = [list(m) for k, m in groupby(puzzle_input[2:], key=bool) if k]
    ranges = [
        [(sds[i], sds[i] + sds[i + 1] - 1) for i in range(len(sds)) if i % 2 == 0]
    ]
    locs = []
    for r in ranges:
        for map in maps:
            r_max = max([int(x[1]) for x in r])
            map = complete_map(r_max, map)
            r = split_ranges(r, map)
            r = [(compute_mapping(x, map), compute_mapping(y, map)) for x, y in r]
        locs += [x for x, _ in r]
    return min(locs)


def compute_mapping(seed: int, map: List[str]) -> int:
    for m in map[1:]:
        d, s, l = [int(x) for x in m.split()]
        if s <= seed < s + l:
            return seed - (s - d)
    return seed


def complete_map(r_max: int, map: List[str]) -> List[str]:
    left = 0
    ordered_s = [
        (int(m.split()[1]), int(m.split()[1]) + int(m.split()[2]) - 1) for m in map[1:]
    ]
    ordered_s.sort()
    for x, y in ordered_s:
        if left < x:
            map.append(f"{left} {left} {x - left - 1}")
        left = y + 1
    if left < r_max:
        map.append(f"{left} {left} {r_max - left - 1}")
    return map


def split_ranges(
    source_ranges: tuple[int, int], map: List[str]
) -> List[tuple[int, int]]:
    locs = []
    for r in source_ranges:
        ranges = []
        left, right = r
        for m in map[1:]:
            _, s, l = [int(x) for x in m.split()]
            if s <= left < s + l:
                if right < s + l:
                    ranges.append((left, right))
                    break
                else:
                    ranges.append((left, s + l - 1))
                    ranges += [*split_ranges([(s + l, right)], map)]
                    break
        locs.append(ranges)
    return [x for sublist in locs for x in sublist]


def read_input_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line.rstrip() for line in f]


if __name__ == "__main__":
    test_input = read_input_file("test_input.txt")
    puzzle_input = read_input_file("input.txt")
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))
