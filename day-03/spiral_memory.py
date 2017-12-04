
import math

def spiral_position(n):
    ring = math.ceil((math.sqrt(n) - 1)/2)
    side = 2 * ring + 1
    max_value = side ** 2

    v = n * 4 // max_value % 4

    if n < max_value - 3 * (side - 1):
        return (ring, n - (max_value - ring - 3 * 2 * ring))
    elif n < max_value - 2 * (side - 1):
        return (max_value - ring - 2 * 2 * ring - n, ring)
    elif n < max_value - 1 * (side - 1):
        return (-ring, max_value - ring - 1 * 2 * ring - n)
    else:
        return (n - (max_value - ring - 0 * 2 * ring), -ring)


manhattan_distance = lambda p: abs(p[0]) + abs(p[1])

def spiral_sum(n):
    values = {(0,0): 1}
    i = 1
    while True:
        pos = spiral_position(i)
        value = sum(values[neighbour] for neighbour in neighbours(pos) if neighbour in values)
        values[pos] = value

        if value > n:
            return value

        i += 1

def neighbours(p):
    return [(p[0] + h, p[1] + v) for h in (-1,0,1) for v in (-1,0,1)]

assert manhattan_distance(spiral_position(1)) == 0
assert manhattan_distance(spiral_position(12)) == 3
assert manhattan_distance(spiral_position(23)) == 2
assert manhattan_distance(spiral_position(1024)) == 31

print(manhattan_distance(spiral_position(312051)))
print(spiral_sum(312051))
