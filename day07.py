
from get_input import *
from collections import defaultdict
import re

DAY = 7

def change_directory(pwd, argument):
    match argument:

        case "..":
            pwd = pwd.rsplit("/", maxsplit=1)[0]
            if len(pwd) == 0:
                pwd = "/"

        case "/":
            pwd = "/"

        case other:
            pwd += f"/{argument}" if len(pwd) > 1 else argument

    return pwd

def part1(data):
    filesystem = defaultdict(int)
    pwd = ""

    for line in data:
        match line.split(" "):

            case ["$", "cd", argument]:
                pwd = change_directory(pwd, argument)

            case [file_size, file_name] if re.match("\d+", file_size):
                # will recurse in reverse to add filename spaces
                _pwd = pwd
                for x in range(_pwd.count("/")):
                    filesystem[_pwd] += int(file_size)
                    _pwd = _pwd.rsplit("/", maxsplit=1)[0]

                if pwd != "/":
                    filesystem["/"] += int(file_size)

            case other:
                ...

    total = sum([v for v in filesystem.values() if v <= 100000])

    return total, filesystem
        


def part2(filesystem, total_disk_space=70000000, required_space=30000000):
    used_space = filesystem["/"]
    needed_space = required_space - (total_disk_space - used_space)
    sizes = [v for v in filesystem.values() if v >= needed_space]
    return sorted(sizes)[0] # smallest directory
    

# Tests
sample = sample_as_lines(DAY)
part1_result = 95437
part2_result = 24933642
part1_total, part1_filesystem = part1(sample)
assert part1_total == part1_result
assert part2(part1_filesystem) == part2_result


data = data_as_lines(DAY)
print("Part 1 Result")
total, filesystem = part1(data)
print(total)

print("Part 2 Result")
print(part2(filesystem))

