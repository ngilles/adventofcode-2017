
from itertools import combinations

test1 = '5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8'
test2 = '5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5'

def parse(data):
    return [[int(cell) for cell in row.split('\t')] for row in data.split('\n')]

with open('input.txt', 'r') as data:
    spreadsheet = parse(data.read())


def checksum1(s):
    return sum(rmax - rmin for rmax, rmin in ((max(r), min(r)) for r in s))

def checksum2(s):
    def find_pair(r):
        for a, b in combinations(r, 2):
            if max(a,b) % min(a, b) == 0:
                return  max(a,b) // min(a,b)

    return sum(find_pair(r) for r in s)

assert checksum1(parse(test1)) == 18
print(checksum1(spreadsheet))

assert checksum2(parse(test2)) == 9
print(checksum2(spreadsheet))
