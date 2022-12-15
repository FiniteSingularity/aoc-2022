"""
Day 14 of Advent of code
https://adventofcode.com/2022/day/14
"""


def read_input(filename: str) -> tuple[list[list[str]], tuple[int, int]]:
    """
    read input
    """
    with open(filename, 'r', encoding='utf-8') as file:
        rock_structures = [[(int(point.split(',')[0]), int(point.split(',')[1])) for point in line.strip().split(" -> ")]
                           for line in file]

    y_max = max([max([point[1] for point in structure])
                for structure in rock_structures]) + 1

    # Calculate the minimum possible value of x, and the maximum
    # possible value of x.  This can change depending on where
    # the max/min x value/height of a ledge is.
    x_min = 500 - y_max
    x_max = 500 + y_max
    for structure in rock_structures:
        for x, y in structure:
            x_right = x + (y_max - y)
            x_left = x - (y_max - y)
            x_min = min(x_left, x_min)
            x_max = max(x_right, x_max)

    # Calculate a shift value to move the minimum value of x to
    # zero.
    x_shift = x_min
    x_max = x_max-x_min+1

    # Initialize the scan placing an air cell '.' in all coordinates.
    scan: list[list[str]] = [
        ['.' for col in range(x_max)] for row in range(y_max+1)
    ]

    # read in the points and connect them.  Place a '#' in occupied cells.
    for structure in rock_structures:
        for pt_1, pt_2 in zip(structure[:-1], structure[1:]):
            for y_pt in range(min(pt_1[1], pt_2[1]), max(pt_1[1], pt_2[1])+1):
                for x_pt in range(min(pt_1[0], pt_2[0]), max(pt_1[0], pt_2[0])+1):
                    scan[y_pt][x_pt-x_shift] = '#'

    return scan, (0, 500-x_shift)


def flow_the_sand(scan: list[list[str]], start_idx: tuple[int, int]) -> tuple[list[list[int]],  int]:
    """
    Flow the sand
    """
    sand_count = 0
    to_the_void = False
    moves: list[tuple[int, int]] = [start_idx]

    while not to_the_void:
        row, col = moves[-1]
        while True:
            if row + 1 >= len(scan):
                to_the_void = True
                break
            below = scan[row+1][col-1:col+2]
            if below[1] == '.':
                row += 1
            elif below[0] == '.':
                row += 1
                col -= 1
            elif below[2] == '.':
                row += 1
                col += 1
            else:
                scan[row][col] = 'O'
                sand_count += 1
                moves.pop()
                break
            moves.append((row, col))
    return scan, sand_count


def flow_the_sand_2(scan: list[list[str]], start_idx: tuple[int, int]) -> tuple[list[list[int]],  int]:
    """
    Flow the sand
    """
    sand_count = 0
    plugged = False
    moves: list[tuple[int, int]] = [start_idx]
    while not plugged:
        row, col = moves[-1]
        while True:
            if row + 1 >= len(scan):
                scan[row][col] = 'O'
                sand_count += 1
                moves.pop()
                break

            below = scan[row+1][col-1:col+2]
            if below[1] == '.':
                row += 1
            elif below[0] == '.':
                row += 1
                col -= 1
            elif below[2] == '.':
                row += 1
                col += 1
            else:
                scan[row][col] = 'O'
                sand_count += 1
                plugged = row == start_idx[0] and col == start_idx[1]
                moves.pop()
                break
            moves.append((row, col))
    return scan, sand_count


def part1() -> None:
    """
    Part 1
    """
    scan, start_idx = read_input("input.txt")
    scan, sand_count = flow_the_sand(scan, start_idx)
    print(sand_count)


def part2() -> None:
    """
    Part 2
    """

    scan, start_idx = read_input("input.txt")
    scan, sand_count = flow_the_sand_2(scan, start_idx)
    print(sand_count)


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
