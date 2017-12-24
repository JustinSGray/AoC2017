import time
import numpy as np

test = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""

real="""31/13
34/4
49/49
23/37
47/45
32/4
12/35
37/30
41/48
0/47
32/30
12/5
37/31
7/41
10/28
35/4
28/35
20/29
32/20
31/43
48/14
10/11
27/6
9/24
8/28
45/48
8/1
16/19
45/45
0/4
29/33
2/5
33/9
11/7
32/10
44/1
40/32
2/45
16/16
1/18
38/36
34/24
39/44
32/37
26/46
25/33
9/10
0/29
38/8
33/33
49/19
18/20
49/39
18/39
26/13
19/32"""


def parse_input(inp):
    lines = inp.split('\n')
    parts = []
    for line in lines: 
        row = line.split("/")
        parts.append(tuple([int(x) for x in row]))

    return parts


data = parse_input(real)

# recurisvely build all possible combinations 

def split(parts, port): 
    ins, outs = [], []
    for p in parts: 
        if port in p: 
            ins.append(p)
        else: 
            outs.append(p)
    return ins, outs

def build(parts, bridge=[], open_port=0): 

    potentials, rest = split(parts, open_port)

    new_bridges = []
    for p in potentials: 
        others = potentials[:]
        others.remove(p)
        others.extend(rest)
        # print(new_parts, p)
        new_bridge = bridge[:]
        new_bridge.append(p)
        new_bridges.append(new_bridge)

        next_port = p[0]
        if p[0] == open_port: 
            next_port = p[1]

        child_bridges = build(others, new_bridge, next_port)
        new_bridges.extend(child_bridges)
        
    return new_bridges

st = time.time()
bs = build(data)
strengths = [np.sum(np.array(x)) for x in bs]


print("part 1", max(strengths))
lenghts = [len(x) for x in bs]

max_length = max(lenghts)
max_l_strenght = 0

for l,s in zip(lenghts, strengths): 
    if l == max_length: 
        max_l_strenght = max([max_l_strenght, s])

print("part2", max_l_strenght)

print('time', time.time() - st)


