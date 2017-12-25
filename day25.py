import numpy as np

# left  --> -1 
# right --> 1

#(current_state, current_value) --> #(write, move, next_state)
test_rules = { 
    ('A',0): (1, 1, 'B'), 
    ('A',1): (0, -1, 'B'), 
    ('B',0): (1, -1, 'A'), 
    ('B',1): (1, 1, 'A')
}

real_rules={
    ('A',0):(1, 1,'B'), 
    ('A',1):(0,-1,'B'),
    ('B',0):(0, 1,'C'),
    ('B',1):(1,-1,'B'),
    ('C',0):(1, 1,'D'),
    ('C',1):(0,-1,'A'),
    ('D',0):(1,-1,'E'),
    ('D',1):(1,-1,'F'),
    ('E',0):(1,-1,'A'),
    ('E',1):(0,-1,'D'),
    ('F',0):(1, 1,'A'),
    ('F',1):(1,-1,'E'),
}


LENGTH = 100000
tape = np.zeros(LENGTH, dtype=int)
cursor = LENGTH//2
state = 'A'

for i in range(12629077): 
    directions = real_rules[state, tape[cursor]]
    tape[cursor] = directions[0]
    cursor += directions[1]
    state = directions[2]


print(np.sum(tape))