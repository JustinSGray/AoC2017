import copy 

def parse_input(input): 
    data = []
    lines = input.split('\n')
    for line in lines: 
        row = [int(x) for x in line.split(':')]
        data.append(row)

    return data

def build_firewall(data): 
    fw = [None,]
    scan_dir = {}
    for depth, scan_range in data: 

        n_fw = len(fw)
        if n_fw <= depth: 
            n_new = depth - n_fw + 1
            fw += n_new*[None,]
        fw[depth] = scan_range*[False,]
        fw[depth][0] = True
        scan_dir[depth] = 1
    return fw, scan_dir

def increment_scanners(fw, scan_dir):
    for i, scanner in enumerate(fw): 
        if scanner is not None: 
            scan_range = len(scanner)
            i_scanner = scanner.index(True)
            scanner[i_scanner] = False
            
            if i_scanner == 0: 
                dir = scan_dir[i] = 1
            elif i_scanner == scan_range - 1: 
                dir = scan_dir[i] = -1
            else: 
                dir = scan_dir[i]

            scanner[i_scanner+dir] = True

def check_caught(depth, fw): 
    scanner = fw[depth]
    if scanner is not None: 
        if scanner[0]: 
            return depth * len(scanner), True
    return 0, False

def walk(fw, scan_dir, fast_quit=False): 
    n_fw = len(fw)
    caughts = []
    any_caught = False
    for depth in range(n_fw): 
        severity, check = check_caught(depth, fw)
        if fast_quit and check: 
            return [1], True
        caughts.append(severity)

        any_caught = any_caught or check
        increment_scanners(fw, scan_dir)

    return caughts, any_caught

def delay(fw, scan_dir): 

    caughts, check = walk(copy.deepcopy(fw), copy.deepcopy(scan_dir), True)
    delay = 0
    while check: 
        increment_scanners(fw, scan_dir)
        caughts, check = walk(copy.deepcopy(fw), copy.deepcopy(scan_dir), True)
        # print('foo', delay, check, sum(caughts)) 

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

    # caughts, check = walk(fw, scan_dir)
    # print('test1 ', caughts, sum(caughts))
    
    fw, scan_dir = build_firewall(test1_data)
    # print('test2 start check', fw)
    print("test2", delay(fw, scan_dir))
    # exit()
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
    fw, scan_dir = build_firewall(real1_data)
    caughts, check = walk(fw, scan_dir)
    print('real1', sum(caughts))

    fw, scan_dir = build_firewall(real1_data)
    print("real2", delay(fw, scan_dir))




