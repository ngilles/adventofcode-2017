
from collections import defaultdict

test = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''

test = open('input.txt', 'r').read()

def _inc(r, v):
    regs[r] += v

def _dec(r, v):
    regs[r] -= v

ops = {
    'inc': _inc,
    'dec': _dec
}

cmps = {
    '>': lambda r, v: regs[r] > v,
    '<': lambda r, v: regs[r] < v,
    '>=': lambda r, v: regs[r] >= v,
    '<=': lambda r, v: regs[r] <= v,
    '==': lambda r, v: regs[r] == v,
    '!=': lambda r, v: regs[r] != v,
}

regs = defaultdict(int)
run_max = None

for line_num, line in enumerate(test.split('\n')):
    line = line.strip()
    try:
        o_r, o_o, o_v, _if, c_r, c_o, c_v = line.split(' ')
    except Exception as e:
        print(line_num, line)
        raise e
    if cmps[c_o](c_r, int(c_v)):
        ops[o_o](o_r, int(o_v))
        run_max = regs[o_r] if run_max is None else max(run_max, regs[o_r])

print(regs)
print(max(regs.items(), key=lambda i: i[1]))
print(run_max)

