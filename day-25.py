

from enum import IntEnum, unique
from collections import defaultdict

@unique
class TMState(IntEnum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5

example_spec = {
    TMState.A: {
        0: (1,  1, TMState.B),
        1: (0, -1, TMState.B),
    },
    TMState.B: {
        0: (1, -1, TMState.A),
        1: (1,  1, TMState.A),
    }
}

spec = {
    TMState.A: {
        0: (1,  1, TMState.B),
        1: (0, -1, TMState.E),
    },
    TMState.B: {
        0: (1, -1, TMState.C),
        1: (0,  1, TMState.A),
    },
    TMState.C: {
        0: (1, -1, TMState.D),
        1: (0,  1, TMState.C),
    },
    TMState.D: {
        0: (1, -1, TMState.E),
        1: (0, -1, TMState.F),
    },
    TMState.E: {
        0: (1, -1, TMState.A),
        1: (1, -1, TMState.C),
    },
    TMState.F: {
        0: (1, -1, TMState.E),
        1: (1,  1, TMState.A),
    },
}

class TuringMachine:
    def __init__(self, spec):
        self._tape = defaultdict(int)
        self._position = 0
        self._state = TMState.A
        self._spec = spec

    @property
    def value(self):
        return self._tape[self._position]
    
    @value.setter
    def value(self, value):
        self._tape[self._position] = value
        

    def move_left(self):
        self._position -= 1

    def move_right(self):
        self._position += 1

    def run(self, steps = 0):
        for _ in range(steps):

            new_value, step, new_state = self._spec[self._state][self.value]
            self.value = new_value
            self._position += step
            self._state = new_state

tm = TuringMachine(spec)
tm.run(12208951)
#tm.run(100)
#print(tm._position, tm._tape)
print(sum(tm._tape.values()))

