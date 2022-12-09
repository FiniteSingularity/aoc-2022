"""
Day 3 of Advent of code
https://adventofcode.com/2022/day/3
"""


def part1() -> None:
    """
    Part 1
    """
    with open("input.txt", "r", encoding="utf-8") as file:
        sacks = [line.strip() for line in file]
        total_priority: int = 0
        for sack in sacks:
            mid = int(len(sack)/2)
            c_1 = set(sack[0:mid])
            c_2 = set(sack[mid:])
            common = list(c_1.intersection(c_2))[0]
            priority = ord(common)-ord("a") + 1 \
                if common.islower() else ord(common)-ord("A") + 27
            total_priority += priority
        print(total_priority)


def part2() -> None:
    """
    Part 2
    """
    with open("input.txt", "r", encoding="utf-8") as file:
        sacks = [line.strip() for line in file]
        total_priority: int = 0
        for group in zip(sacks[::3], sacks[1::3], sacks[2::3]):
            c_1 = set(group[0])
            c_2 = set(group[1])
            c_3 = set(group[2])
            common = list(c_1.intersection(c_2.intersection(c_3)))[0]
            priority = ord(common)-ord("a") + 1 \
                if common.islower() else ord(common)-ord("A") + 27
            total_priority += priority
    print(total_priority)


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
