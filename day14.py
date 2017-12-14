
import numpy as np 

import networkx as nx

from day10 import multi_hasher


SIZE=128

def count_row(key, n_row): 

    inp = '{}-{}'.format(key,n_row)
    hash = multi_hasher(inp)
    bin_hash = ''.join([bin(int(char, 16))[2:].zfill(4) for char in hash])
    return bin_hash, bin_hash.count('1')

def count_all(key): 
    tot = 0
    mat = []
    for i in range(128): 
        row, n_1 = count_row(key, i)
        tot += n_1
        mat.append(row)
    return tot, mat

    return 0



def get_neigbors(mat, i, j): 

    if mat[i][j] == 0: 
        return []  

    neighbors = []
    top = (i-1,j)
    if top[0] >=0:
        if mat[top[0]][top[1]] == "1": 
            neighbors.append(top)
    
    left = (i, j-1)
    if left[1] >=0:
        if mat[left[0]][left[1]] == "1": 
            neighbors.append(left)
    
    right = (i, j+1)
    if right[1] < SIZE:
        if mat[right[0]][right[1]] == "1": 
            neighbors.append(right)

    bot = (i+1, j)        
    if bot[0] < SIZE:
        if mat[bot[0]][bot[1]] == "1": 
            neighbors.append(bot)

    return neighbors


def get_neighbors_recurse(mat, i, j, cur_neighbors=set()):
    
    neighbors = set(get_neigbors(mat, i, j))
    new_neighbors = neighbors.difference(cur_neighbors)
    cur_neighbors.update(neighbors)
    for n in new_neighbors: 
        child_neigbors = get_neighbors_recurse(mat, n[0], n[1], cur_neighbors)
        cur_neighbors.update(child_neigbors)

    return cur_neighbors

def count_islands(mat): 

    block_map = np.zeros((SIZE,SIZE),dtype=int)

    for i,row in enumerate(mat): 
        for j,col in enumerate(row): 
            if col == "1": 
                block_id = i*SIZE + j + 1
                neighbors = get_neighbors_recurse(mat, i, j, set())
                for loc in neighbors: 
                    block_map[loc[0], loc[1]] = block_id
                block_map[i,j] = block_id
    print(block_map[:8,:8])

    blocks = block_map[block_map>0]
    return len(set(blocks))

if __name__ == "__main__": 

    test1_input = "flqrgnkx"

    print('test1 hash', multi_hasher(test1_input+"-0"))
    print('test1 hex to bin e', "{0:04b}".format(int('e', 16)), '1110')    
    print('test1 hex to bin f', "{0:04b}".format(int('f', 16)), '1111')
    print('test1 hex to bin f', "{0:04b}".format(int('0', 16)), '0000')
    print('test1 hex to bin a', "{0:04b}".format(int('a', 16)), '1010')
    print('test1 hex to bin a0c2017', "{0:04b}".format(int('a0c2017', 16)).ljust(8*4-1,'0')== '1010000011000010000000010111000')
    # exit()

    count, mat = count_all(test1_input)

    data = []
    for row in mat: 
        data.append([int(s) for s in row])
    data = np.array(data)
    print(data[:8,:8])

    print('test1 check', count)
    print(get_neigbors(mat, 1, 7))
    n_i = count_islands(mat)
    print('test2 check', n_i)

    count, mat = count_all('jzgqcdpd')
    print('real1', count)
    print('real2', count_islands(mat))



