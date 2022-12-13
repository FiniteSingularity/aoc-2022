"""
Day 13 of Advent of code
https://adventofcode.com/2022/day/13
"""

import json
import functools


def read_input(filename):
    """
    Read in the input file, convert to list of ints and lists
    """
    packets = []
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            packet_1 = file.readline().strip()
            if not packet_1:
                break
            packet_2 = file.readline().strip()
            file.readline()
            packets.append((json.loads(packet_1), json.loads(packet_2)))
    return packets


def read_input_2(filename):
    """
    Convert input to necessary structure for part 2
    """
    return [a for b in read_input(filename) for a in b]


def check_packets(packets):
    """
    Checks validity of all sets of packets
    """
    packets_valid: list[bool] = []

    for packet_set in packets:
        packets_valid.append(check_packet_order(packet_set))

    return packets_valid


def check_packet_order(packet_set) -> str:
    """
    Checks for proper packet orrder
    """
    for i, left_val in enumerate(packet_set[0]):
        if len(packet_set[1]) - 1 < i:  # we know right is shorter than left
            return 'invalid'
        right_val = packet_set[1][i]

        if isinstance(left_val, list) or isinstance(right_val, list):
            # Folks!  WE HAVE A LIST
            if not isinstance(left_val, list):
                left_val = [left_val]
            if not isinstance(right_val, list):
                right_val = [right_val]
            validity = check_packet_order((left_val, right_val))
            if validity == 'valid' or validity == 'invalid':
                return validity
        else:
            if left_val < right_val:
                return 'valid'
            if right_val < left_val:
                return 'invalid'

    if len(packet_set[0]) < len(packet_set[1]):
        return 'valid'

    return 'keep_checking'


def packet_compare(a, b):
    """
    Packet Compare
    """
    valid = check_packet_order((a, b))
    return -1 if valid == 'valid' else 1


def part1() -> None:
    """
    Part 1
    """
    packets = read_input("input.txt")
    validity = check_packets(packets)
    print(sum([i+1 for i, val in enumerate(validity) if val == 'valid']))


def part2() -> None:
    """
    Part 2
    """
    packets = read_input_2("input.txt") + [[[2]], [[6]]]
    packets.sort(key=functools.cmp_to_key(packet_compare))
    print((packets.index([[2]])+1) * (packets.index([[6]])+1))


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
