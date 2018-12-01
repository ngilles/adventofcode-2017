

score = 0
depth = 0
gc = 0

data = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
data = open('input.txt', 'r').read()

state = 'NORMAL'

for c in data:
    if state == 'NORMAL':
        if c == '{':
            depth += 1
        elif c == '}':
            score += depth
            depth -= 1
        elif c == '<':
            state = 'GARBAGE'
    elif state == 'GARBAGE':
        if c == '!':
            state = 'GARBAGE_SKIP'
        elif c == '>':
            state = 'NORMAL'
        else:
            gc += 1
    elif state == 'GARBAGE_SKIP':
        state = 'GARBAGE'

print(score)
print(gc)
