class Afn:
    def __init__(self, transition_function, init_state, ok_states):
        self.transition_function = transition_function
        self.init_state = init_state
        self.ok_states = ok_states
        
    def read_in(self, in_str):
        current_states = {self.init_state}
        for char in in_str:
            next_states = set()
            for state in current_states:
                next_states |= self.transition_function.get((state, char), set())
            current_states = next_states
        return any(state in self.ok_states for state in current_states)

transition_function = {
    (0, 'a'): {1},
    (0, 'b'): {0},
    (1, 'a'): {2},
    (1, 'b'): {0},
    (2, 'a'): {2},
    (2, 'b'): {3},
    (3, 'a'): {3},
    (3, 'b'): {3},
}

init_state = 0
ok_states = {0, 2, 3}
str_in = str(input("Enter the corresponding character: "))
automaton = Afn(transition_function, init_state, ok_states)
print(automaton.read_in(str_in))