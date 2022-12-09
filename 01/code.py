"""
Day 1 of Advent of code
"""


def part1() -> None:
    """
    Part 1
    """
    max_val: int = -99999

    file = open('input.txt', 'r', encoding="utf-8")
    lines = file.readlines()

    cur_sum: int = 0
    for line in lines:
        if line.strip() != '':
            cur_sum += int(line.strip())
            max_val = max(max_val, cur_sum)
        else:
            cur_sum = 0

    print(max_val)


def part2() -> None:
    """
    Part 2
    """
    file = open('input.txt', 'r', encoding="utf-8")
    lines = file.readlines()

    totals: list[int] = [0]
    for line in lines:
        if line.strip() != '':
            totals[-1] += int(line.strip())
        else:
            totals.append(0)
    totals.sort()
    print(sum(totals[-3:]))


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
