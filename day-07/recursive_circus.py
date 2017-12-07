
import re
from collections import defaultdict, Counter
from operator import eq

test_data = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''


program_pattern = re.compile(r'(?P<name>.+) \((?P<weight>\d+)\)(?: -> (?P<children>.*))?')

class Program:
    def __init__(self, name=None, weight=None, parent=None):
        self.name = name
        self.weight = weight
        self.parent = parent

        self.children = set()
        self.weight_total = 0



def parse_program(l):
    m = program_pattern.match(l)
    if m:
        info = m.groupdict()
        return info['name'], int(info['weight']), set(c.strip() for c in info['children'].split(',')) if info['children'] is not None else set()
    else:
        raise ValueError(repr(l))


def build_towers(data):
    programs = defaultdict(Program)

    for name, weight, children in data:
        program = programs[name]

        program.name = name
        program.weight = weight

        children = {programs[child] for child in children}
        program.children.update(children)
        for child in children:
            child.parent = program

    return programs

def build_weights(root):

    if len(root.children) == 0:
        root.total_weight = root.weight
    else:
        root.total_weight = sum(build_weights(child) for child in root.children) + root.weight

    return root.total_weight

def find_root(programs):
    # Take an node and walk up to the parent
    program = programs[list(programs.keys())[0]]
    while program.parent is not None: program = program.parent

    return program


def find_unbalanced(root):

    # Find off child:
    counts = Counter(c.total_weight for c in root.children)
    odd_weight = next((w for w, c in counts.items() if c == 1), None)
    if odd_weight is None:
        return root # I'm the odd one
    else:
        odd_child = next(c for c in root.children if c.total_weight == odd_weight)
        return find_unbalanced(odd_child)

def weight_diff(program):
    siblings = program.parent.children
    other = next(s for s in siblings if s is not program)
    return other.total_weight - program.total_weight




test_data = [parse_program(l.strip()) for l in test_data.split('\n')]

with open('input.txt', 'r') as f:
    data = [parse_program(l.strip('\n')) for l in f.readlines()]



# Testing
test_programs = build_towers(test_data)
test_root = find_root(test_programs)
build_weights(test_root)
unbalanced_root = find_unbalanced(test_root)
test_weight = unbalanced_root.weight + weight_diff(unbalanced_root)

assert test_root.name == 'tknk'
assert test_weight == 60

programs = build_towers(data)
root = find_root(programs)
build_weights(root)
unbalanced_root = find_unbalanced(root)
weight = unbalanced_root.weight + weight_diff(unbalanced_root)

print(root)
print(weight)
