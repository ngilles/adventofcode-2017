



def twist(l, pos, length):
    if pos + length > len(l):
        over = pos + length - len(l)
        #print('over=', over)
        #print('l   =', l)
        tmp = l[pos:] + l[:pos]
        #print('tmpa=', tmp)
        twist(tmp, 0, length)
        #print('tmpb=', tmp)
        tmp = tmp[length-over:] + tmp[:length-over]
        #print('tmpc=', tmp)
        l[:] = tmp[:]

    else:
        l[pos: pos+length] = reversed(l[pos:pos+length])

l = list(range(256))
#l = list(range(5))

pos = 0
ss = 0
#swaps = [ord(v) for v in 'AoC 2017']
swaps = [ord(v) for v in open('input.txt', 'r').read()]

swaps += [17, 31, 73, 47, 23]

print(swaps)

for rounds in range(64):
    for swap in swaps:
        #print('----------')
        #print(pos, swap, ss)
        twist(l, pos, swap)
        #print(l)
        pos = (pos + swap + ss) % len(l)
        ss += 1

print(l)
print(l[0] * l[1])

dig = ''.join('%0.2x' % b for b in [reduce(lambda a,b: a ^ b, l[block:block+16]) for block in range(0,255,16)])
print(dig)






