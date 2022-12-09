"""
Day 2 of Advent of code
https://adventofcode.com/2022/day/2
"""

lose = [2, 3, 1]
win = [3, 1, 2]


def part1() -> None:
    """
    Part 1
    """
    total: int = 0
    with open("input.txt", "r", encoding="utf-8") as f:
        games = [line.strip().split(" ") for line in f]
        for game in games:
            val = ord(game[1]) - ord("W")
            opp_val = ord(game[0]) - ord("A") + 1
            if val == opp_val:
                val += 3
            elif lose[val-1] == opp_val:
                val += 0
            else:
                val += 6
            total += val

    print(total)


def part2() -> None:
    """
    Part 2
    """
    total: int = 0
    with open("input.txt", "r", encoding="utf-8") as f:
        games = [line.strip().split(" ") for line in f]
        for game in games:
            result = ord(game[1]) - ord("W")
            opp_val = ord(game[0]) - ord("A") + 1
            if result == 1:
                val = win[opp_val - 1]
            elif result == 2:
                val = opp_val
            else:
                val = lose[opp_val - 1]
            total += val + (result - 1) * 3

    print(total)


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
