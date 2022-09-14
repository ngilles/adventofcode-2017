data = [
    '32/31',
    '2/2',
    '0/43',
    '45/15',
    '33/24',
    '20/20',
    '14/42',
    '2/35',
    '50/27',
    '2/17',
    '5/45',
    '3/14',
    '26/1',
    '33/38',
    '29/6',
    '50/32',
    '9/48',
    '36/34',
    '33/50',
    '37/35',
    '12/12',
    '26/13',
    '19/4',
    '5/5',
    '14/46',
    '17/29',
    '45/43',
    '5/0',
    '18/18',
    '41/22',
    '50/3',
    '4/4',
    '17/1',
    '40/7',
    '19/0',
    '33/7',
    '22/48',
    '9/14',
    '50/43',
    '26/29',
    '19/33',
    '46/31',
    '3/16',
    '29/46',
    '16/0',
    '34/17',
    '31/7',
    '5/27',
    '7/4',
    '49/49',
    '14/21',
    '50/9',
    '14/44',
    '29/29',
    '13/38',
    '31/11',
]

# data = [
#     '0/2',
#     '2/2',
#     '2/3',
#     '3/4',
#     '3/5',
#     '0/1',
#     '10/1',
#     '9/10',
# ]



from collections import defaultdict

by_pins = defaultdict(set)
for l in data:
    a, b = [int(e) for e in l.split('/')]
    by_pins[a].add(b)
    by_pins[b].add(a)
    

current = 0
used = set()
def build_birdge(current, connectors):
    length, strength, used, open_end = current or (0, 0, set(), 0)

    for c in connectors[open_end]:
        next_connector = (open_end, c) if open_end <= c else (c, open_end) # connecter, in canonical orientation
        if next_connector not in used:
            new_bridge = length + 1, strength + open_end + c, (used | {next_connector}), c

            yield new_bridge
            yield from build_birdge(new_bridge, connectors)

from pprint import pprint
bridges = [b for b in build_birdge(None, by_pins)]

#pprint(bridges)
print(max(bridges, key=lambda b: b[1]))
print(max(bridges, key=lambda b: (b[0], b[1])))

