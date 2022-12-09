"""
Day 5 of Advent of code
https://adventofcode.com/2022/day/5
"""


def process_input(filename: str) -> tuple[list[list[str]], list[list[int]]]:
    """
    Processes input file
    """
    stacks: list[list[str]] = []
    with open(filename, "r", encoding='utf-8') as file:
        line = file.readline()
        while line[0:2] != " 1":
            vals = [line[i:i+4].strip().replace("[", "").replace("]", "")
                    for i in range(0, len(line), 4)]
            for i, val in enumerate(vals):
                if len(stacks) == i:
                    stacks.append([])
                if val != "":
                    stacks[i].append(val)
            line = file.readline()
        file.readline()
        commands: list[list[int]] = []
        while True:
            line = file.readline()
            if not line:
                break
            line = line.strip().replace("move ", "").replace(
                " from ", ",").replace(" to ", ",")
            commands.append([int(val) for val in line.split(",")])
    return (stacks, commands)


def part1() -> None:
    """
    Part 1
    """
    stacks, commands = process_input("input.txt")

    for command in commands:
        moving = stacks[command[1]-1][0:command[0]]
        stacks[command[1]-1] = stacks[command[1]-1][command[0]:]
        stacks[command[2]-1] = moving[::-1] + stacks[command[2]-1]

    for stack in stacks:
        if len(stack) > 0:
            print(stack[0], end='')
    print("")


def part2() -> None:
    """
    Part 2
    """
    stacks, commands = process_input("input.txt")

    for command in commands:
        moving = stacks[command[1]-1][0:command[0]]
        stacks[command[1]-1] = stacks[command[1]-1][command[0]:]
        stacks[command[2]-1] = moving + stacks[command[2]-1]

    for stack in stacks:
        if len(stack) > 0:
            print(stack[0], end='')
    print("")


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
