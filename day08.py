
from get_input import *
import math

DAY = 8

def max_or_minus(x):
    return max(x) if x else -1 # -1 will be an edge

def scan_grid(grid):
    for current_row, row_contents in enumerate(grid):
        for current_column, col_contents in enumerate(row_contents):
            current_value = grid[current_row][current_column]
            col_slice = [row[current_column] for row in grid]
            row_slice = grid[current_row]
            up = col_slice[:current_row] 
            down = col_slice[current_row+1:] 
            left = row_slice[:current_column] 
            right = row_slice[current_column+1:] 
            yield current_value, up, down, left, right

def part1(data):
    # first, put the data in a grid
    grid = [[int(c) for c in line] for line in data] # access as grid[row][col]

    total = 0

    for current_value, up, down, left, right in scan_grid(grid):
        max_tree_heights = map(max_or_minus, [up, down, left, right])
        if any(map(lambda x: current_value > x, max_tree_heights)):
            total += 1

    return total

def part2(data):
    # will need to reverse up and left
    grid = [[int(c) for c in line] for line in data] # access as grid[row][col]

    highest_scenic_score = 0

    for current_value, up, down, left, right in scan_grid(grid):
        scores = []
        
        # these are reversed so they can be searched from source to end
        up.reverse()
        left.reverse()

        for direction in [up, down, left, right]:
            direction_score = 0

            for tree in direction:

                if tree >= current_value:
                    direction_score += 1
                    break # can't see anymore trees after this

                elif tree < current_value:
                    direction_score += 1

            scores.append(direction_score)
        
        if (scenic_score := math.prod(scores)) > highest_scenic_score:
            highest_scenic_score = scenic_score

    return highest_scenic_score


# Tests
sample = sample_as_lines(DAY)
part1_result = 21
part2_result = 8
assert part1(sample) == part1_result
assert part2(sample) == part2_result

data = data_as_lines(DAY)
print("Part 1 Result")
print(part1(data))

print("Part 2 Result")
print(part2(data))

