
from collections import defaultdict

data = '''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5'''

data = open('input.txt', 'r').read()

neighbours = defaultdict(set)

for line in data.split('\n'):
    line = line.strip()
    try:
        node, adj = line.split('<->')
    except:
        print(line)
        raise
    node = int(node)
    for n in adj.split(','):
        neighbours[node].add(int(n))

visited = set()


def visit(start):
    visited.add(start)
    for n in neighbours[start]:
        if n not in visited:
            visit(n)

groups = 0
for node in neighbours:
    if node not in visited:
        groups += 1
        visit(node)

print(len(visited))
print(groups)


