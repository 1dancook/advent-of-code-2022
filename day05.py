import re
from collections import defaultdict
from get_input import *

DAY = 5

MOVE_LINE = re.compile('(move\s)(?P<move>\d+)(\sfrom\s)(?P<from>\d+)(\sto\s)(?P<to>\d+)')

def split_data(data):
    return re.split('\n\s\d\s.*\n',data)

def make_containers(containers):
    d = defaultdict(list)

    for line in containers.splitlines():
        for x in range(0, len(line)+1, 4):
            container = int((x/4) + 1)
            value = line[x:x+4].strip().replace("[","").replace("]","")
            if value:
                d[container].append(value)

    # reverse all the containers
    for container in d.values():
        container.reverse()

    return d

def part1(data):

    containers, instructions = split_data(data)

    d = make_containers(containers)

    for line in instructions.splitlines():
        if (m := re.match(MOVE_LINE, line)):
            move = int(m.group("move"))
            t = int(m.group("to"))
            f = int(m.group("from"))
            for x in range(move):
                d[t].append(d[f].pop())

    # get the top crate in each container, in right order
    return ''.join([d[i].pop() for i in sorted(d.keys())])


def part2(data):
    containers, instructions = split_data(data)

    d = make_containers(containers)

    for line in instructions.splitlines():
        if (m := re.match(MOVE_LINE, line)):
            move = int(m.group("move"))
            t = int(m.group("to"))
            f = int(m.group("from"))
            s = len(d[f])-move # get difference for slicing the list
            for item in d[f][s:]:
                d[t].append(item)
            d[f] = d[f][:s]
            
    return ''.join([d[i].pop() for i in sorted(d.keys())])


# Tests

sample = get_sample_input(DAY, strip=False)
part1_result = "CMZ"
part2_result = "MCD"
assert part1(sample) == part1_result
assert part2(sample) == part2_result


data = get_input(DAY, strip=False)
print("Part 1 Result")
print(part1(data))

print("Part 2 Result")
print(part2(data))

