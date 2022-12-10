"""
Day 10 of Advent of code
https://adventofcode.com/2022/day/10
"""


def read_input(filename: str) -> list[tuple[str, int]]:
    """
    Read Input File.
    """
    instructions: list[tuple[str, int]] = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip().split(" ")
            if line[0] == 'noop':
                instructions.append(('noop', 0))
            else:
                instructions.append((line[0], int(line[1])))
    return instructions


def calculate_register(instructions: list[tuple[str, int]]):
    """
    Calculates the register history given a list of instructions
    index is cycle - 1
    """

    ecks_values = [1]  # This *should* be 90, but AoC didnt :(
    for instruction in instructions:
        if instruction[0] == 'noop':
            ecks_values.append(ecks_values[-1])
        elif instruction[0] == 'addx':
            ecks_values.append(ecks_values[-1])
            ecks_values.append(ecks_values[-1]+instruction[1])
    return ecks_values


def part1() -> None:
    """
    Part 1
    """
    instructions = read_input("input.txt")

    ecks_values = calculate_register(instructions)

    strength_sum = sum([(val+1) * ecks_values[val]
                       for val in [19, 59, 99, 139, 179, 219]])
    print(strength_sum)
    return


def part2() -> None:
    """
    Part 2
    """
    instructions = read_input("input.txt")
    ecks_values = calculate_register(instructions)

    width = 40
    height = 6

    row = -1
    for i in range(width*height):
        if i % 40 == 0:
            row += 1
            print("")
        current_value = ecks_values[i]
        if i % 40 >= current_value - 1 and i % 40 <= current_value + 1:
            print("#", end="")
        else:
            print(".", end="")
    print("")
    return


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
