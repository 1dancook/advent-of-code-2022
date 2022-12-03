from get_input import *

DAY = 3

def part1(data):
    total = 0
    for line in data:
        l = len(line)//2
        c = ({c for c in line[l:]} & {c for c in line[:l]}).pop()
        total += ord(c) - 96 if ord(c) >= 97 else ord(c) - 38
    return total


def part2(data):
    data = data.splitlines()
    groups = [data[i:i+3] for i in range(0,len(data),3)]
    total = 0
    for group in groups:
        c = (set(group[0]) & set(group[1]) & set(group[2])).pop()
        total += ord(c) - 96 if ord(c) >= 97 else ord(c) - 38
    return total


# Tests
sample = sample_as_lines(DAY)
part1_result = 157
assert part1(sample) == part1_result

sample = get_sample_input(DAY)
part2_result = 70
assert part2(sample) == part2_result


data = data_as_lines(DAY)
print("Part 1 Result")
print(part1(data))

data = get_input(DAY)
print("Part 2 Result")
print(part2(data))

