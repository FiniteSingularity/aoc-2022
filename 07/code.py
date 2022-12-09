"""
Day 7 of Advent of code
"""


def build_tree(filename: str) -> dict:
    """
    Build the file tree
    """
    file_tree = {}
    with open(filename, 'r', encoding='utf-8') as file:
        current_directory = ""
        for line in file:
            line = line.strip().split(" ")
            if line[1] == "cd":
                cd = line[2]
                if cd == "/":
                    current_directory = "/"
                elif cd == "..":
                    current_directory = file_tree[current_directory]["parent"]
                    continue
                else:
                    current_directory = f"{current_directory}/{cd}"

                if current_directory not in file_tree:
                    file_tree[current_directory] = {
                        "parent": "",
                        "size": 0
                    }
            elif line[1] == "ls":
                pass
            elif line[0] == "dir":
                dir_name = f"{current_directory}/{line[1]}"
                if dir_name not in file_tree:
                    file_tree[dir_name] = {
                        "parent": current_directory,
                        "size": 0
                    }
                else:
                    file_tree[dir_name]["parent"] = current_directory
            else:
                file_size = int(line[0])
                file_tree[current_directory]["size"] += file_size
                parent_dir = file_tree[current_directory]["parent"]
                while parent_dir != "":
                    file_tree[parent_dir]["size"] += file_size
                    parent_dir = file_tree[parent_dir]["parent"]
    return file_tree


def part1() -> None:
    """
    Part 1
    """
    file_tree = build_tree("input.txt")
    total = sum([int(dir["size"])
                 for i, dir in file_tree.items() if int(dir["size"]) <= 100000])
    print(total)
    return


def part2() -> None:
    """
    Part 2
    """
    file_tree = build_tree("input.txt")
    dir_sizes = [int(dir["size"])
                 for i, dir in file_tree.items()]
    unused = 70000000 - file_tree["/"]["size"]
    needed = 30000000
    dir_sizes = [int(dir["size"])
                 for i, dir in file_tree.items() if int(dir["size"]) >= needed - unused]
    print(min(dir_sizes))


if __name__ == "__main__":
    print("---- Part 1 ----")
    part1()
    print("---- Part 2 ----")
    part2()
