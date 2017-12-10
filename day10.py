import numpy as np
from functools import reduce 

def hasher(input, n, start_pos=0, start_skip=0, start_hash=None): 
    
    lengths = [int(s) for s in input.split(",")]
    if start_hash is None: 
        hash = list(range(n))
    else: 
        hash = start_hash
    pos = start_pos

    for skip,l in enumerate(lengths): 
        start = pos 
        end = (pos+l)
        part =[hash[j%(n)] for j in range(start, end)]
        # print(hash)
        # print(pos, skip, l, "|", start, end, part)
        for j,val in zip(range(start,end), part[::-1]): 
            j_circ = j%n
            hash[j_circ] = val
        pos = (pos+l + skip+start_skip)%n
        # print(hash)
        # print()
    return hash, hash[0]*hash[1], pos, skip+1+start_skip


def prep_input(line): 
    return ",".join([str(ord(s)) for s in line]+['17','31','73','47','23'])

def dense_hash(sparse_hash, n=16): 
    d_hash = []
    for i in range(n): 
        start = 16*i
        end = start + 16
        part = sparse_hash[start:end]
        d = reduce(lambda x,y: x^y, part)
        d_hash.append(d)

    return d_hash

def to_hex(ints): 
    hexs = []
    for num in ints: 
        h = hex(num)[2:]
        if len(h) == 1: 
            hh = '0%s'%h
        else: 
            hh = h
        hexs.append(hh)
    return "".join(hexs)


def multi_hasher(input, n=256): 

    mod_input = prep_input(input)

    hash, checksum, pos, skip = hasher(mod_input, n)

    for counter in range(63): 
        hash, checksum, pos, skip = hasher(mod_input, n, start_pos=pos, start_skip=skip, start_hash=hash)

    d_hash = dense_hash(hash)
    h_hash = to_hex(d_hash)

    return h_hash
if __name__ == "__main__": 



    test1_input = """3, 4, 1, 5"""
    print('test1', hasher(test1_input, 5))

    real_input = """212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164"""
    # ans = hasher(real_input, 256)
    # print('real1', ans[1],ans[2], ans[3])

    test2_input = """3, 4, 1, 5, 17, 31, 73, 47, 23"""
    test2_ascii_check = """1,2,3"""
    print('test2 ascii check', prep_input(test2_ascii_check))

    test2_dhash = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
    print('test2 dense_hash check', dense_hash(test2_dhash, 1))

    print('test2 hex_check', to_hex([64, 7, 255]))

    print('test2 check1', multi_hasher(""))
    print('test2 check2', "AoC 2017", multi_hasher("AoC 2017"))
    print('real2', multi_hasher(real_input))


