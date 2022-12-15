"""
Day 15 of Advent of code
https://adventofcode.com/2022/day/15
"""

ROW_NUM = 2000000

MIN_X = 0
MAX_X = 4000000
MIN_Y = 0
MAX_Y = 4000000


def build_sensor(sensor_data):
    """
    Build Sensor
    """
    sensor = (sensor_data[0], sensor_data[1])
    beacon = (sensor_data[2], sensor_data[3])
    manhattan_distance = sum([abs(pt_1-pt_2)
                             for pt_1, pt_2 in zip(sensor, beacon)])
    return {
        "sensor": sensor,
        "beacon": beacon,
        "manhattan_distance": manhattan_distance,
        "x_range": (sensor[0]-manhattan_distance, sensor[0]+manhattan_distance),
        "y_range": (sensor[1]-manhattan_distance, sensor[1]+manhattan_distance)
    }


def get_x_range(sensor, row_num):
    """
    Get X Range
    """
    dist = abs(row_num-sensor["sensor"][1])
    dist_x = sensor["manhattan_distance"]-dist
    return (sensor["sensor"][0]-dist_x, sensor["sensor"][0]+dist_x)


def combined_ranges(ranges):
    """
    Combine Ranges
    """
    ranges = sorted(ranges)
    combined = [list(ranges[0])]
    for rang in ranges[1:]:  # 1  5   2 3
        if rang[0] <= combined[-1][1] + 1 and rang[1] >= combined[-1][1]:
            combined[-1][1] = rang[1]
        elif rang[1] > combined[-1][1]:
            combined.append(list(rang))
    return combined


def read_input(filename):
    """
    Read Input
    """
    with open(filename, 'r', encoding='utf-8') as file:
        sensors = [[int(val) for val in line.strip().replace("Sensor at x=", "").replace(
            ", y=", ",").replace(": closest beacon is at x=", ",").split(",")] for line in file]

        sensors = [build_sensor(sensor) for sensor in sensors]

    return sensors


def part1() -> None:
    """
    Part 1
    """
    sensors = read_input("input.txt")

    # for sensor in sensors:
    #     print(sensor)

    sensors_in_row = [sensor for sensor in sensors if sensor["y_range"]
                      [0] <= ROW_NUM and sensor["y_range"][1] >= ROW_NUM]

    ranges = [get_x_range(sensor, ROW_NUM) for sensor in sensors_in_row]

    ranges = combined_ranges(ranges)

    count = sum([(rang[1]-rang[0]+1) for rang in ranges])

    beacon_count = len(set([
        sensor["beacon"] for sensor in sensors if sensor["beacon"][1] == ROW_NUM]))

    print(count - beacon_count)

    return


def part2() -> None:
    """
    Part 2
    """
    sensors = read_input("input.txt")

    for row_num in range(MAX_Y+1):
        sensors_in_row = [sensor for sensor in sensors if sensor["y_range"]
                          [0] <= row_num and sensor["y_range"][1] >= row_num]
        sensors_in_row = [sensor for sensor in sensors_in_row if sensor["x_range"]
                          [1] >= MIN_X and sensor["x_range"][0] <= MAX_X]
        ranges = [get_x_range(sensor, row_num) for sensor in sensors_in_row]
        ranges = combined_ranges(ranges)
        if len(ranges) > 1:
            point = (ranges[0][1]+1, row_num)
            break

    print(4000000 * point[0] + point[1])

    return


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
