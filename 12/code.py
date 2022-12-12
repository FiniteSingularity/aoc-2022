"""
Day 12 of Advent of code
https://adventofcode.com/2022/day/12
"""

from queue import PriorityQueue


class HeightMap:
    """
    Class describing the graph between all points in the
    height map.
    """

    def __init__(self, num_points: int):
        self.points: int = num_points
        self.step_cost: list[any] = [{} for i in range(num_points)]
        self.visited: list[int] = []
        self.start_point = -1
        self.end_point = -1

    def add_step(self, a, b, cost):
        """
        Add a step in the height map
        """
        self.step_cost[a][b] = cost


def read_input(filename) -> tuple[list[list[int]], tuple[int, int], tuple[int, int]]:
    """
    Read the input file and returns the points read, start point, and end point
    """
    points: list[list[int]] = []
    start = (-1, -1)
    end = (-1, -1)
    with open(filename, 'r', encoding='utf-8') as file:
        for row, line in enumerate(file):
            points.append([])
            for col, char in enumerate(line.strip()):
                if char == 'S':
                    start = (row, col)
                    char = 'a'
                elif char == 'E':
                    end = (row, col)
                    char = 'z'
                points[-1].append(ord(char)-ord('a'))
    return points, start, end


def read_input_1(filename) -> tuple[HeightMap, list[list[int]]]:
    """
    Sets up input for part 1
    """
    points, start, end = read_input(filename)
    col_size = len(points[0])
    num_points = len(points) * col_size
    height_map = HeightMap(num_points)
    height_map.start_point = start[0] * col_size + start[1]
    height_map.end_point = end[0] * col_size + end[1]

    for i, row in enumerate(points):
        for j, val in enumerate(row):
            idx = i * col_size + j
            # step up
            if i > 0 and points[i-1][j] <= val + 1:
                height_map.add_step(idx, (i-1)*col_size + j, 1)
            if i < len(points) - 1 and points[i+1][j] <= val + 1:
                height_map.add_step(idx, (i+1)*col_size + j, 1)
            if j > 0 and points[i][j-1] <= val + 1:
                height_map.add_step(idx, i*col_size + j - 1, 1)
            if j < col_size - 1 and points[i][j+1] <= val + 1:
                height_map.add_step(idx, i*col_size + j + 1, 1)

    return height_map, points


def read_input_2(filename) -> tuple[HeightMap, list[list[int]]]:
    """
    Sets up input for part 2
    Here we reverse the step direction- Valid steps
    from high points towards low.
    """
    points, start, end = read_input(filename)
    col_size = len(points[0])
    num_points = len(points) * col_size
    height_map = HeightMap(num_points)
    height_map.start_point = start[0] * col_size + start[1]
    height_map.end_point = end[0] * col_size + end[1]

    for i, row in enumerate(points):
        for j, val in enumerate(row):
            idx = i * col_size + j
            # step up (for reverse search)
            if i > 0 and points[i-1][j] <= val + 1:
                height_map.add_step((i-1)*col_size + j, idx, 1)
            if i < len(points) - 1 and points[i+1][j] <= val + 1:
                height_map.add_step((i+1)*col_size + j, idx, 1)
            if j > 0 and points[i][j-1] <= val + 1:
                height_map.add_step(i*col_size + j - 1, idx, 1)
            if j < col_size - 1 and points[i][j+1] <= val + 1:
                height_map.add_step(i*col_size + j + 1, idx, 1)

    return height_map, points


def dijkstra(height_map: HeightMap):
    """
    Implements dijkstra's algorithm to calculate the shortest path
    to height_map.end_point
    """
    height_map.visited = []
    dist = {idx: 1.e99 for idx in range(height_map.points)}
    dist[height_map.start_point] = 0

    queue = PriorityQueue()
    queue.put((0, height_map.start_point))

    while not queue.empty():
        _, current = queue.get()
        height_map.visited.append(current)

        # Early exit if our current point is the end_point.
        # We have found the shortest path.
        if current == height_map.end_point:
            return dist[current]

        for neighbor, cost in height_map.step_cost[current].items():
            if neighbor not in height_map.visited:
                old_cost = dist[neighbor]
                new_cost = dist[current]+cost
                if new_cost < old_cost:
                    queue.put((new_cost, neighbor))
                    dist[neighbor] = new_cost

    return 1e99  # Return huge number as no path to end was found.


def dijkstra_min(height_map: HeightMap, min_points: list[int]):
    """
    Implements dijkstra's algorithm search for the shortest minimum starting
    point
    """
    height_map.visited = []
    dist = {idx: 1.e99 for idx in range(height_map.points)}
    dist[height_map.end_point] = 0

    queue = PriorityQueue()
    queue.put((0, height_map.end_point))

    while not queue.empty():
        _, current = queue.get()
        height_map.visited.append(current)

        # Early exit if the current point is in our
        # list of min_points (with altitude "a")
        # By definition, the first of these points found
        # will be the minimum path to any of the low points
        if current in min_points:
            return dist[current]

        for neighbor, cost in height_map.step_cost[current].items():
            if neighbor not in height_map.visited:
                old_cost = dist[neighbor]
                new_cost = dist[current]+cost
                if new_cost < old_cost:
                    queue.put((new_cost, neighbor))
                    dist[neighbor] = new_cost

    return dist


def part1() -> None:
    """
    Part 1
    """
    height_map, _ = read_input_1("input.txt")
    print(dijkstra(height_map))
    return


def part2() -> None:
    """
    Part 2
    """

    height_map, points = read_input_2("input.txt")
    points = [point for row in points for point in row]
    start_points = [idx for idx, point in enumerate(
        points) if point == 0]

    print(dijkstra_min(height_map, start_points))

    return


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
