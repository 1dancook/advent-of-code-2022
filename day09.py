
from get_input import *

DAY = 9

class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return str((self.x, self.y))

def get_directions(data):
    for line in data:
        direction, steps = line.split(" ")
        for _ in range(int(steps)):
            step = 1 if direction in ["R", "U"] else -1
            x = step if direction in ["R", "L"] else 0 # horizontal
            y = step if direction in ["U", "D"] else 0 # vertical
            yield x,y


def move_knot(knot, previous_knot):
    x_proximity = previous_knot.x - knot.x
    y_proximity = previous_knot.y - knot.y

    # is knot close enough to previous_knot?
    if -1 <= x_proximity <= 1 and -1 <= y_proximity <= 1:
        return # don't move

    # same horizontal row
    elif previous_knot.x == knot.x:
        if y_proximity <= -2:
            knot.y -= 1
        elif y_proximity >= 2:
            knot.y += 1

    # same vertical column
    elif previous_knot.y == knot.y:
        if x_proximity <= -2:
            knot.x -= 1
        elif x_proximity >= 2:
            knot.x += 1

    # are they on a diagonal?
    elif (previous_knot.x != knot.x) and (previous_knot.y != knot.y):
        match [x_proximity, y_proximity]:
            case [1,2] | [2,1] | [2,2]:
                knot.x += 1
                knot.y += 1
            case [-1,2] | [-2,1] | [-2, 2]:
                knot.x -= 1
                knot.y += 1
            case [1,-2] | [2,-1] | [2, -2]:
                knot.x += 1
                knot.y -= 1
            case [-1,-2] | [-2,-1] | [-2,-2]:
                knot.x -= 1
                knot.y -= 1


def get_tail_positions(data, number_of_knots=2):
    knots = [Knot() for n in range(number_of_knots)]
    tail_positions = set()
    for x, y in get_directions(data):

        for k, knot in enumerate(knots):

            if k == 0:
                knot.x += x
                knot.y += y
                continue

            move_knot(knot, knots[k-1])

            if k == len(knots) - 1:
                tail_positions.add((knot.x, knot.y))

    # return the number of unique tail positions
    return len(tail_positions)

def part1(data):
    return get_tail_positions(data, number_of_knots=2)

def part2(data):
    return get_tail_positions(data, number_of_knots=10)


# Tests
sample = sample_as_lines(DAY)
part1_result = 13
assert part1(sample) == part1_result

part2_result = 36 

# there was a second sample set given for part 2
sample2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".strip().splitlines()
assert part2(sample2) == part2_result


data = data_as_lines(DAY)
print("Part 1 Result")
print(part1(data)) # 6642

print("Part 2 Result")
print(part2(data)) # 2765
