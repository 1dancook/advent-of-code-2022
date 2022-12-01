from get_input import *

i = get_input(1)

result = [
        sum(
            [int(elf) for elf in group.strip().splitlines()]
            )
        for
        group 
        in i.split("\n\n")
        ]

# part 1
print(max(result))

# part 2
print(sum(sorted(result, reverse=True)[0:3]))


