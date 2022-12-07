from get_input import *

DAY = 6

def part1(data, distinct=4):
    for x in range(0, len(data) - distinct):
        if len(set(data[x:x + distinct])) == distinct:
            return x + distinct

# Tests
sample = get_sample_input(DAY)
part1_result = 7
part2_result = 19
assert part1(sample) == part1_result
assert part1(sample, distinct=14) == part2_result


data = get_input(DAY)
print("Part 1 Result")
print(part1(data))

print("Part 2 Result")
print(part1(data, distinct=14))

