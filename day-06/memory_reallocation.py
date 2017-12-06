

def redistribute(banks):
    max_idx = banks.index(max(banks))

    blocks = banks[max_idx]
    banks[max_idx] = 0

    # probably can be done as a closed-form expression per bank?
    for i in range(blocks):
        banks[(max_idx + 1 + i) % len(banks)] += 1


def reallocate(banks):
    seen_states = set()
    seen_states.add(tuple(banks))

    it = 1

    while True:
        redistribute(banks)
        new_state = tuple(banks)

        if new_state in seen_states:
            return it
        else:
            seen_states.add(new_state)
            it += 1


test_banks = [0, 2, 7, 0]

with open('input.txt', 'r') as f:
    data = [int(v) for v in f.read().split('\t')]

assert reallocate(test_banks) == 5
print(reallocate(data))


# second call will find loop size

assert reallocate(test_banks) == 4
print(reallocate(data))





