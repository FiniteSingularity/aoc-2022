"""
Day 8 of Advent of code
https://adventofcode.com/2022/day/8
"""

import itertools
import math


def read_input(filename: str) -> list[list[int]]:
    """
    Read Input File into Grid
    """
    grid: list[list[int]] = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            grid.append([int(val) for val in line.strip()])

    return grid


def transpose(grid: list[list[int]]) -> list[list[int]]:
    """
    Transpose the list of lists
    """
    return [
        [row[i] for row in grid] for i in range(0, len(grid))
    ]


def generate_hidden_map(grid: list[list[int]]) -> list[list[int]]:
    """
    Generate map of max tree
    """
    left = [
        [-1] + list(itertools.accumulate(row, max))[:-1] for row in grid
    ]

    right = [
        list(reversed([-1] + list(itertools.accumulate(row[::-1], max))))[1:] for row in grid
    ]

    grid_t = transpose(grid)
    up = transpose([
        [-1] + list(itertools.accumulate(row, max))[:-1] for row in grid_t
    ])

    down = transpose([
        list(reversed([-1] + list(itertools.accumulate(row[::-1], max))))[1:] for row in grid_t
    ])

    max_map = [[min(val) for val in zip(left[i], right[i], up[i], down[i])]
               for i in range(len(left))]
    hidden = [[0 if row[0][col] <= row[1][col] else 1 for col in range(
        len(row[0]))] for row in list(zip(grid, max_map))]
    return hidden


def distance_to_obstruction(height_list: list[int], height: int) -> int:
    """
    calculate distance to obstructing tree
    """
    for i, val in enumerate(height_list):
        if val >= height:
            return i+1
    return len(height_list)


def gen_scenic_scores(grid: list[list[int]]) -> list[list[int]]:
    """
    Calculate the scenic scores for each grid point
    """
    left = [
        [
            distance_to_obstruction(row[:i][::-1], row[i]) for i in range(len(row))
        ] for row in grid
    ]
    right = [
        [
            distance_to_obstruction(row[i+1:], row[i]) for i in range(len(row))
        ] for row in grid
    ]
    grid_t = transpose(grid)
    up = transpose([
        [
            distance_to_obstruction(row[:i][::-1], row[i]) for i in range(len(row))
        ] for row in grid_t
    ])
    down = transpose([
        [
            distance_to_obstruction(row[i+1:], row[i]) for i in range(len(row))
        ] for row in grid_t
    ])

    scores = [[math.prod(col) for col in zip(left[i], right[i], up[i], down[i])]
              for i in range(len(left))]

    return scores


def part1() -> None:
    """
    Part 1
    """
    grid = read_input("test.txt")
    hidden = generate_hidden_map(grid)
    print(sum(map(sum, hidden)))
    return


def part2() -> None:
    """
    Part 2
    """
    grid = read_input("input.txt")
    scores = gen_scenic_scores(grid)
    print(max(map(max, scores)))
    return


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
