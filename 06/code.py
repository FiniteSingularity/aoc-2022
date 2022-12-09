"""
Day 6 of Advent of code
https://adventofcode.com/2022/day/6
"""


def marker_search(filename: str, marker_length: int) -> int:
    """
    Search for a marker with  length marker_length
    """
    with open(filename, "r", encoding="utf-8") as file:
        line = file.readline()
        for i in range(0, len(line)-marker_length):
            if len(set(line[i:i+marker_length])) == marker_length:
                return i+marker_length


def part1() -> None:
    """
    Part 1
    """
    print(marker_search("input.txt", 4))


def part2() -> None:
    """
    Part 2
    """
    print(marker_search("input.txt", 14))


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
