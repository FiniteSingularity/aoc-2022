"""
Day 4 of Advent of code
https://adventofcode.com/2022/day/4
"""


def part1() -> None:
    """
    Part 1
    """
    with open("input.txt", "r", encoding="utf-8") as file:
        pairs = [[[int(assign.split('-')[0]), int(assign.split('-')[1])] for assign in line.strip().split(",")]
                 for line in file]
        total: int = 0
        for pair in pairs:
            if (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]) or (pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]):
                total += 1
        print(total)


def part2() -> None:
    """
    Part 2
    """
    with open("input.txt", "r", encoding="utf-8") as file:
        pairs = [[[int(assign.split('-')[0]), int(assign.split('-')[1])] for assign in line.strip().split(",")]
                 for line in file]
        total: int = 0
        for pair in pairs:
            if pair[0][1] < pair[1][0] or pair[0][0] > pair[1][1]:
                pass
            else:
                total += 1
        print(total)


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
