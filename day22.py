import numpy as np 

test = """..#
#..
..."""

real = """...###.#.#.##...##.#..##.
.#...#..##.#.#..##.#.####
#..#.#...######.....#####
.###.#####.#...#.##.##...
.#.#.##......#....#.#.#..
....##.##.#..##.#...#....
#...###...#.###.#.#......
..#..#.....##..####..##.#
#...#..####.#####...#.##.
###.#.#..#..#...##.#..#..
.....##..###.##.#.....#..
#.....#...#.###.##.##...#
.#.##.##.##.#.#####.##...
##.#.###..#.####....#.#..
#.##.#...#.###.#.####..##
#.##..#..##..#.##.####.##
#.##.#....###.#.#......#.
.##..#.##..###.#..#...###
#..#.#.#####.....#.#.#...
.#####..###.#.#.##..#....
###..#..#..##...#.#.##...
..##....##.####.....#.#.#
..###.##...#..#.#####.###
####.########.#.#..##.#.#
#####.#..##...####.#..#.."""


def parse_input(inp, label): 
    size = 10000
    half_size = size//2

    grid = np.zeros((size+1,size+1), dtype=int)
    
    center = half_size 

    lines =[]
    for line in inp.split("\n"): 
        lines.append([int(char=="#")*label for char in line])

    n_start = len(lines)
    delta = (n_start-1)//2
    start_low = center-delta
    start_high = center+delta+1

    grid[start_low:start_high, start_low:start_high] = lines

    return grid, center






def part1(inp ):

    grid, center = parse_input(inp,1) 
    cur_x = center
    cur_y = center
    cur_dir =  0 #0->up , 1->left, 2->down, 3->right
    # left is +1 
    #right is -1

    move_map = {
        0:(0,-1), 
        1:(-1,0), 
        2:(0,1), 
        3:(1,0)
    }

    n_states = 2

    infection_counter = 0
    for i in range(10000):
        # print(i, cur_x, cur_y, grid[cur_y, cur_x], cur_dir)
        if grid[cur_y, cur_x]%n_states: # infected -> clean and turn right
            cur_dir = (cur_dir-1)%4
            # print("    right")

        else: # clean -> infect and turn left
            cur_dir = (cur_dir+1)%4
            infection_counter += 1
            # print("    left")
        grid[cur_y, cur_x] = (grid[cur_y, cur_x]+1)%n_states
        # print('  ', cur_dir)
        move = move_map[cur_dir]
        cur_x += move[0]
        cur_y += move[1]

    # print(grid)
    print(infection_counter)



def part2(inp): 
    grid, center = parse_input(inp,2) 

    cur_x = center
    cur_y = center
    cur_dir =  0 #0->up , 1->left, 2->down, 3->right
    # left is +1 
    #right is -1

    # 0 -> clean, 1-> weak, 2-> infected, 3-> flagged

    # fist one is state, second is direction

    move_map = {
        0:(0,-1), 
        1:(-1,0), 
        2:(0,1), 
        3:(1,0)
    }

    change_map = {
        (0,0):1, 
        (0,1):2, 
        (0,2):3, 
        (0,3):0, 

        (1,0):0, 
        (1,1):1, 
        (1,2):2, 
        (1,3):3, 

        (2,0):3, 
        (2,1):0, 
        (2,2):1, 
        (2,3):2, 

        (3,0):2,
        (3,1):3,
        (3,2):0,
        (3,3):1,
    }

    n_states = 4

    infection_counter = 0
    for i in range(10000000):
        # print(i, cur_x, cur_y, grid[cur_y, cur_x], cur_dir)
        
        cur_dir = change_map[grid[cur_y, cur_x], cur_dir]
        move = move_map[cur_dir]
        # print("  ", move, cur_dir)

        grid[cur_y, cur_x] = (grid[cur_y, cur_x]+1)%n_states
        if (grid[cur_y, cur_x] % n_states) == 2: 
            infection_counter += 1

        cur_x += move[0]
        cur_y += move[1]

        # print(grid)
        # print()
    print(infection_counter)

part1(real)
part2(real)


