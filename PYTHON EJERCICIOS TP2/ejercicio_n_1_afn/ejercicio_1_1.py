class Afn:
    def __init__(self, transitions, initial_state, ok_states):
        self.transitions = transitions
        self.intial_state = initial_state
        self.ok_states = set(ok_states)
        "self.in_str = in_str"
    
    def read_in (self, in_str):
        current = set([self.intial_state])
        for char in in_str:
            next_state = set()
            for state in current:
                if (state, char) in self.transitions:
                    next_state |= self.transitions[(state, char)]
                current = next_state
        return bool(current & self.ok_states)

marks = {
    (0, 'a'): {0,1},
    (0, 'b'): {0,1},
    (1, 'a'): {1},
    (1, 'b'): {1},}
start_state = 0
ok_states = {0,1}
in_str = str(input("Enter the corresponding character: "))
automation = Afn(marks, start_state, ok_states)
print(automation.read_in(in_str))