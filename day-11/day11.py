
from __future__ import print_function

import math

motion = {
    'n': (0, -1, +1),
    'nw': (-1, 0, +1),
    'ne': (+1, -1, 0),
    's': (0, +1, -1),
    'sw': (-1, +1, 0),
    'se': (+1, 0, -1)
}

data = [
    ('ne,ne,ne', 3),
    ('ne,ne,sw,sw', 0),
    ('ne,ne,s,s', 2),
    ('se,sw,se,sw,sw', 3)
]

data.append((open('input.txt', 'r').read().strip(), 0))



def dist_to_center(pos):
    return max(abs(pos), abs(a.y - b.y), abs(a.z - b.z))

for moves, result in data:
    pos = (0, 0, 0)
    max_dist = 0
    for direction in moves.split(','):
        direction = direction.strip()
        move = motion[direction]
        pos = pos[0] + move[0], pos[1] + move[1], pos[2] + move[2]
        max_dist = max(max_dist, abs(pos[0]), abs(pos[1]), abs(pos[2]))

    dist = max(abs(p) for p in pos)
    
    # Print final pos, dist, expected
    print(pos, max_dist, dist, '=', result)


