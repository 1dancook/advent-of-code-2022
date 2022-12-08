from get_input import *
from collections import defaultdict
from copy import deepcopy

DAY = 7

def make_filesystem(data):
    filesystem = defaultdict(int)
    pwd = []

    for line in data:
        match line.split(" "):

            case ["$", "cd", ".."]:
                pwd.pop()

            case ["$", "cd", directory_name] if directory_name != "/":
                pwd.append(directory_name)

            case [file_size, file_name] if file_size[0].isdigit():
                # reverse recursion to add the file size to PWD and all parents directories
                file_size = int(file_size)
                temp_pwd = deepcopy(pwd)
                for x in range(len(temp_pwd)):
                    directory = "/" + "/".join(temp_pwd)
                    filesystem[directory] += file_size
                    temp_pwd.pop()
                filesystem["/"] += file_size

    return filesystem

def part1(filesystem):
    total = sum([v for v in filesystem.values() if v <= 100000])
    return total

def part2(filesystem, total_disk_space=70000000, required_space=30000000):
    used_space = filesystem["/"]
    needed_space = required_space - (total_disk_space - used_space)
    sizes = [v for v in filesystem.values() if v >= needed_space]
    return sorted(sizes)[0] # smallest directory
    
# Tests
fs = make_filesystem(sample_as_lines(DAY))
part1_result = 95437
part2_result = 24933642
assert part1(fs) == part1_result
assert part2(fs) == part2_result

fs = make_filesystem(data_as_lines(DAY))
print("Part 1 Result")
total = part1(fs)
print(total) #2031851

print("Part 2 Result")
print(part2(fs)) #2568781

