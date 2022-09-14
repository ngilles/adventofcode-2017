import numpy as np

expansions = {}

def S(a):
    return ''.join(a.flatten())

with open('input.txt') as puzzle_input:
    for l in puzzle_input:
        pattern_in, pattern_out = [
            np.array([
                list(s) for s in b.strip().split('/')
            ])
            for b in l.split('=>')
        ]
        #print(f'{pattern_in!r} {pattern_out!r}')
#        expansions[pattern_in.data.tobytes()] = pattern_out

        # map pattern expansions + rotated versions
        expansions[S(pattern_in)] = pattern_out
        expansions[S(np.rot90(pattern_in, k=1))] = pattern_out
        expansions[S(np.rot90(pattern_in, k=2))] = pattern_out
        expansions[S(np.rot90(pattern_in, k=3))] = pattern_out

        # map flipped /rotated pattern expansions
        pattern_flipped = np.fliplr(pattern_in)
        expansions[S(pattern_flipped)] = pattern_out
        expansions[S(np.rot90(pattern_flipped, k=1))] = pattern_out
        expansions[S(np.rot90(pattern_flipped, k=2))] = pattern_out
        expansions[S(np.rot90(pattern_flipped, k=3))] = pattern_out


init = np.array([
    ['.', '#', '.'],
    ['.', '.', '#'],
    ['#', '#', '#'],
])

curr = init
print(curr)
for _ in range(18):
    side = np.shape(curr)[0]
    step = 2 if side % 2 == 0 else 3
    expanded_side = side // step * (step+1)

    new_array = np.full((expanded_side, expanded_side), '.')
    
    for i in range(0, side, step):
        for j in range(0, side, step):
            ni = i // step * (step+1)
            nj = j // step * (step+1)
            pattern = curr[i:i+step, j:j+step]
            expansion = expansions[S(pattern)]
            new_array[ni:ni+step+1, nj:nj+step+1] = expansion

    curr = new_array
    print(curr)

print(np.count_nonzero(curr == '#'))