from get_input import *

DAY = 2

points = {
        65: 1, #rock (A)
        66: 2, #paper (B)
        67: 3, #scissors (C)
        }

# A B C  -- beats bottom row
# C A B

def caeser(num, skip=1, start=65, end=67):
    if num == end:
        return start + skip - 1
    elif num + skip > end:
        return start + ((num + skip) - end) - 1
    return num + skip


def part1(data):
    total = 0
    for line in data.splitlines():
        a, b = line.strip().split(" ")
        a = ord(a)
        b = ord(b) - 23
        total += points[b]
        if a == b:
            # draw, 3 points
            total += 3
        elif a == caeser(b):
            # loss, 0 points
            total += 0
        elif b == caeser(a):
            # win, 6 points
            total += 6
    return total


def part2(data):
    total = 0
    for line in data.splitlines():
        a, outcome = line.strip().split(" ")
        a = ord(a)
        b = ""
        if outcome == "Y": #end in draw
            b = a
            total += 3
        elif outcome == "X": # lose
            b = caeser(a, skip=2)
        elif outcome == "Z": # win
            b = caeser(a)
            total += 6
        total += points[b]
    return total


# Tests
sample = get_sample_input(DAY)
part1_result = 15
part2_result = 12
assert part1(sample) == part1_result
assert part2(sample) == part2_result


data = get_input(DAY)
print("Part 1 Result")
print(part1(data))

print("Part 2 Result")
print(part2(data))

