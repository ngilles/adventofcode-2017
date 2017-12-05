

def twisty_trampoline1(t):
    ip = 0
    ic = 0

    while 0 <= ip < len(t):
        jmp = t[ip]
        t[ip] += 1  # increment by one after each jump
        ip += jmp
        ic += 1

    return ic

def twisty_trampoline2(t):
    ip = 0
    ic = 0

    while 0 <= ip < len(t):
        jmp = t[ip]
        t[ip] += 1 if jmp < 3 else -1
        ip += jmp
        ic += 1

    return ic


with open('input.txt', 'r') as f:
    data = [int(l.strip()) for l in f.readlines()]


assert twisty_trampoline1([0, 3, 0, 1, -3]) == 5

print(twisty_trampoline1(data[:]))


assert twisty_trampoline2([0, 3, 0, 1, -3]) == 10

print(twisty_trampoline2(data[:]))


