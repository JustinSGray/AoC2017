import copy 

def parse_input(input): 
    data = []
    lines = input.split('\n')
    for line in lines: 
        row = [int(x) for x in line.split(':')]
        data.append(row)

    return data


def check_caught(depth, s_range, delay):
    if (depth+delay) % ((s_range-1)*2) == 0: 
        return depth*s_range, True
    return 0, False

def walk(data, fast_quit=False, delay=0): 
    
    caughts = []
    any_caught = False
    for depth, s_range in data: 
        severity, check = check_caught(depth, s_range, delay)
        if fast_quit and check: 
            return [1], True
        caughts.append(severity)

        any_caught = any_caught or check

    return caughts, any_caught

def find_delay(data): 

    delay = 0
    while True: 
        severity, check = walk(data, fast_quit=True, delay=delay)
        if not check: 
            break 
        delay += 1
        
    return delay

if __name__ == "__main__":

    test1_input ="""0: 3
1: 2
4: 4
6: 4"""

    # print("test1 parse", parse_input(test1_input))
    test1_data = parse_input(test1_input)
    # fw, scan_dir = build_firewall(test1_data)
    # print('test1 struct', fw, scan_dir)

    caughts, check = walk(test1_data)
    print('test1 ', caughts, sum(caughts))

    # print('test2 start check', fw)
    print("test2", find_delay(test1_data))
    real_input = """0: 3
1: 2
2: 5
4: 4
6: 4
8: 6
10: 6
12: 6
14: 8
16: 6
18: 8
20: 8
22: 8
24: 12
26: 8
28: 12
30: 8
32: 12
34: 12
36: 14
38: 10
40: 12
42: 14
44: 10
46: 14
48: 12
50: 14
52: 12
54: 9
56: 14
58: 12
60: 12
64: 14
66: 12
70: 14
76: 20
78: 17
80: 14
84: 14
86: 14
88: 18
90: 20
92: 14
98: 18"""

    real1_data = parse_input(real_input)
    caughts, check = walk(real1_data)
    print('real1', sum(caughts))

    
    print("real2", find_delay(real1_data))




