data = [
    '#.#...###.#.##.#....##.##',
    '..####.#.######....#....#',
    '###..###.#.###.##.##..#.#',
    '...##.....##.###.##.###..',
    '....#...##.##..#....###..',
    '##.#..###.#.###......####',
    '#.#.###...###..#.#.#.#.#.',
    '###...##..##..#..##......',
    '##.#.####.#..###....#.###',
    '.....#..###....######..##',
    '.##.#.###....#..#####..#.',
    '########...##.##....##..#',
    '.#.###.##.#..#..#.#..##..',
    '.#.##.##....##....##.#.#.',
    '..#.#.##.#..##..##.#..#.#',
    '.####..#..#.###..#..#..#.',
    '#.#.##......##..#.....###',
    '...####...#.#.##.....####',
    '#..##..##..#.####.#.#..#.',
    '#...###.##..###..#..#....',
    '#..#....##.##.....###..##',
    '#..##...#...##...####..#.',
    '#.###..#.#####.#..#..###.',
    '###.#...#.##..#..#...##.#',
    '.#...#..#.#.#.##.####....',
]

# data = [
#     '..#',
#     '#..',
#     '...',
# ]

from enum import IntEnum, unique
from collections import defaultdict, Counter

directions = [
    (-1, 0), # up
    (0, 1), # right
    (1, 0), # down
    (0, -1), # left
]

@unique
class NodeState(IntEnum):
    clean = 0
    weakend = 1
    infected = 2
    flagged = 3

infected = {(i, j) for i, r in enumerate(data) for j, v in enumerate(r) if v == '#'}
infection_count = 0
print(infected)
direction = 0
position = ((len(data)-1) // 2, (len(data[0])- 1) // 2)

# print(position)

# for _ in range(10000):
#     if position in infected:
#         direction = (direction + 1) % 4
#         infected.remove(position)
#     else:
#         direction = (direction - 1) % 4
#         infected.add(position)
#         infection_count += 1

#     position = (position[0] + directions[direction][0], position[1] + directions[direction][1])

# print(position)
# print(len(infected))
# print(infection_count)

nodes = defaultdict(lambda: NodeState.clean)
nodes |= {(i, j): NodeState.infected for i, r in enumerate(data) for j, v in enumerate(r) if v == '#'}

for _ in range(10000000):
    if nodes[position] is NodeState.clean:
        direction = (direction - 1) % 4
        nodes[position] = NodeState.weakend
    elif nodes[position] is NodeState.weakend:
        # no direction change
        nodes[position] = NodeState.infected
        infection_count += 1
    elif nodes[position] is NodeState.infected:
        direction = (direction + 1) % 4
        nodes[position] = NodeState.flagged
    elif nodes[position] is NodeState.flagged:
        direction = (direction + 2) % 4
        nodes[position] = NodeState.clean
        # could delete instead for memory?
        # del nodes[position]
    else:
        raise Exception('boom')

    position = (position[0] + directions[direction][0], position[1] + directions[direction][1])

print(position)
print(Counter(nodes.values()))
print(infection_count)
