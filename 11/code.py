"""
Day 11 of Advent of code
https://adventofcode.com/2022/day/11
"""

from typing import TypedDict
import math


class Monkey(TypedDict):
    """
    Monkey TypedDict type.
    """
    items: list[int]
    operation: tuple[str, int]
    test: int
    throw_to: tuple[int, int]
    inspected: int


def read_input(filename) -> list[Monkey]:
    """
    Read Input File.  list of Monkey
    """

    monkeys = []
    with open(filename, 'r', encoding='utf-8') as file:
        monkey_id = int(file.readline().strip().replace(":", "").split(" ")[1])
        while monkey_id >= 0:
            items = [int(item) for item in file.readline().strip().replace(
                "Starting items: ", "").split(", ")]
            op, op_val = file.readline().strip().replace(
                "Operation: new = old ", "").split(" ")
            if op_val == "old":
                op = "pow"
                op_val = 2
            test = int(file.readline().strip().split(" ")[-1])
            throw_true = int(file.readline().strip().split(" ")[-1])
            throw_false = int(file.readline().strip().split(" ")[-1])
            monkeys.append({
                "items": items,
                "operation": (op, int(op_val)),
                "test": test,
                "throw_to": (throw_true, throw_false),
                "inspected": 0
            })

            file.readline()
            line = file.readline()
            if line:
                monkey_id = int(line.strip().replace(
                    ":", "").split(" ")[1])
            else:
                monkey_id = -1

    return monkeys


def calculate_worry(monkey: Monkey, item: int, relief: int) -> int:
    """
    Calculate worry level given a monkey and an item
    """

    if monkey["operation"][0] == '+':
        worry = item + monkey["operation"][1]
    elif monkey["operation"][0] == '*':
        worry = item * monkey["operation"][1]
    else:
        worry = item ** 2

    return math.floor(worry/relief)


def process_rounds(monkeys: list[Monkey], relief: int, rounds: int) -> list[Monkey]:
    """
    Processes rounds of monkey business
    """

    worry_scale = 1
    for monkey in monkeys:
        worry_scale *= monkey["test"]

    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey["items"]:
                monkey["inspected"] += 1
                worry = calculate_worry(monkey, item, relief)
                worry %= worry_scale
                if worry % monkey["test"] == 0:
                    throw_to = 0
                else:
                    throw_to = 1

                monkeys[monkey["throw_to"][throw_to]]["items"].append(worry)

            monkey["items"] = []
    return monkeys


def part1() -> None:
    """
    Part 1
    """
    monkeys = read_input("input.txt")
    monkeys = process_rounds(monkeys, 3, 20)

    inspections = [monkey["inspected"] for monkey in monkeys]
    inspections.sort()
    print(inspections[-1]*inspections[-2])


def part2() -> None:
    """
    Part 2
    """
    monkeys = read_input("input.txt")
    monkeys = process_rounds(monkeys, 1, 10000)

    inspections = [monkey["inspected"] for monkey in monkeys]
    inspections.sort()
    print(inspections[-1]*inspections[-2])


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
