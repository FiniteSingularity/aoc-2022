"""
Day 9 of Advent of code
https://adventofcode.com/2022/day/9
"""


MOVE_MAP: dict[str, tuple[int, int]] = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}


def sign(value: int) -> int:
    """
    Returns the sign of an integer:
    -1 for negative values
    0 for zero values
    1 for positive values
    """
    return (value > 0) - (value < 0)


def read_input(filename: str) -> list[tuple[int, int]]:
    """
    Read Input File.  Return step-by-step positions of the rope head.
    """
    h_positions: list[tuple[int, int]] = [(0, 0)]
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            dir_str, dist_str = line.split(" ")
            # Get unit movement from MOVE_MAP
            unit_move: tuple[int, int] = MOVE_MAP[dir_str]
            for _ in range(int(dist_str)):
                last_position = h_positions[-1]
                # At each step, append last position + unit movement
                h_positions.append(
                    (last_position[0] + unit_move[0],
                     last_position[1] + unit_move[1])
                )
        return h_positions


def get_t_positions(h_positions: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Gets T positions from list of H positions.  Assumes knot count of 2
    (only H followed directly by T)
    """
    t_positions: list[tuple[int, int]] = [h_positions[0]]
    for h_position in h_positions[1:]:
        last_t_position = t_positions[-1]

        # element-wise subtraction of two tuples
        delta = (h_position[0]-last_t_position[0],
                 h_position[1]-last_t_position[1])

        # if we are more than 1 space away in any direction, calculate
        # new position of tail.
        if max((abs(delta[0]), abs(delta[1]))) > 1:
            # get sign -1, 0, 1 for delta_x and delta_y
            d_x, d_y = sign(delta[0]), sign(delta[1])
            # append element-wise addition of two last position and (d_x, d_y)
            t_positions.append(
                (last_t_position[0] + d_x, last_t_position[1] + d_y)
            )
    return t_positions


def part1() -> None:
    """
    Part 1
    """
    h_positions = read_input("input.txt")
    t_positions = get_t_positions(h_positions)

    # Print the tail position set length
    # i.e. the number of unique locations of the tail
    print(len(set(t_positions)))


def part2() -> None:
    """
    Part 2
    """
    h_positions = read_input("input.txt")

    # Iterate over the number of knots, assume head is the
    # prior calculated knot position.
    for _ in range(9):
        t_positions = get_t_positions(h_positions)
        h_positions = t_positions

    # Print the final tail position set length
    # i.e. the number of unique locations of the tail
    print(len(set(t_positions)))


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
