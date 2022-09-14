data = [
    'set b 9',  # b = 99
    'set c 9',   # c = b (99)
    'jnz a 2',   # if a != 0: goto non_debug 
    'jnz 1 5',   # goto big_loop
# non_debug:
    'mul b 100',      # b = b * 100 (9900)
    'sub b -100000',  # b = b + 100000 (109900)
    'set c b',        # c = b (109900)
    'sub c -17000',   # c = c + 17000 (126900)
# big_loop:
    'set f 1',    # f = 1
    'set d 2',    # d = 2
# loop_1
    'set e 2',    # e = 2
    'set g d',    # |
    'mul g e',    # |
    'sub g b',    # g = (d * e) - b
    'jnz g 2',    # if g != 0: goto loop_2
    'set f 0',    #
# loop_2
    'sub e -1',   # inc e
    'set g e',    # |
    'sub g b',    # g = e - b
    'jnz g -8',   # if g != 0: goto loop_1
    'sub d -1',   # inc d
    'set g d',    # |
    'sub g b',    # g = d - b
    'jnz g -13',  # if g != 0: goto loop_1
    'jnz f 2',    # if f != 0: goto loop_3
    'sub h -1',   # inc h
# loop_3
    'set g b',    # |
    'sub g c',    # g = b - c
    'jnz g 2',    # if g != 0: goto loop_4
    'jnz 1 3',    # END
# loop_4
    'sub b -17',  # 
    'jnz 1 -23',  # got big_loop
]

# b = 99
# c = 99
# f = 1
# d = 2
# e = 2
# g = (d * e) - b
# if g == 0 :
#   f = 0
# e += 1
# g = e - b
# if g 
import time
from collections import defaultdict

program = [e.split() for e in data]

class CPU:
    def __init__(self, program, registers={}):
        self._program = program
        self._ip = 0
        self._registers = {r: 0 for r in 'abcdefgh'} | registers
        self._instruction_counters = defaultdict(int)
        self._instruction_count = 0
        self._ip_counters = [0] *  len(program)

        self._breakpoints = {0, 4, 5, 6, 7,  8}
    
        print(self._registers)
    def run(self):
        while True:
            if self._ip >= len(self._program):
                print('------------------')
                print(self._registers)
                print(self._ip_counters)
                print(self._instruction_counters)
                raise Exception('ended')

            if self._instruction_count == 0:
                print('------------------')
                print(self._registers)
                print(self._ip_counters)
                print(self._instruction_counters)

            self._instruction_count = (self._instruction_count + 1)  % 1000
            
            offset = 1
            instruction, op1, op2 = self._program[self._ip]
            self._ip_counters[self._ip] += 1
            self._instruction_counters[instruction] += 1
            if instruction == 'set':
                self._registers[op1] = int(self._registers.get(op2, op2))
            if instruction == 'sub':
                self._registers[op1] -= int(self._registers.get(op2, op2))
            if instruction == 'mul':
                self._registers[op1] *= int(self._registers.get(op2, op2))
            if instruction == 'jnz':
                if int(self._registers.get(op1, op1)) != 0:
                    offset = int(self._registers.get(op2, op2))

            # debug
            # for idx, inst in enumerate(self._program):
            #     print('   ' if idx != self._ip else '-->', inst)
            # print()
            # print('ip:', self._ip, self._registers)
            # time.sleep(0.1)
            # if self._ip in self._breakpoints:
            #     input('continue...')

            self._ip += offset

cpu = CPU(program, {'a': 1})
#cpu.run()
h = 0
for x in range(109900,126900 + 1,17):
	for i in range(2,x):
		if x % i == 0:
			h += 1
			break
print(h)