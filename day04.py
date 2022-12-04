from get_input import *

DAY = 4

def pairs_to_sets(line):
    parts = line.split(",")
    a_range = [int(x) for x in parts[0].split("-")]
    b_range = [int(x) for x in parts[1].split("-")]
    a = {x for x in range(a_range[0], a_range[1] + 1)}
    b = {x for x in range(b_range[0], b_range[1] + 1)}
    return a, b

def part1(data):
    total = 0
    for line in data:
        a, b = pairs_to_sets(line)
        if a.issubset(b) or b.issubset(a):
            total += 1
    return total

def part2(data):
    total = 0
    for line in data:
        a, b = pairs_to_sets(line)
        if a & b:
            total += 1
    return total


# Tests
sample = sample_as_lines(DAY)
part1_result = 2
part2_result = 4
assert part1(sample) == part1_result
assert part2(sample) == part2_result


data = data_as_lines(DAY)
print("Part 1 Result")
print(part1(data))

print("Part 2 Result")
print(part2(data))

