from math import *

def spiral(num): 

    if num == 1: 
        return (0, 0)

    iter_num = 1
    j_num = 0
    upper = iter_num**2
    while upper < num:
        iter_num += 2 
        upper = iter_num**2
        j_num += 1 

    lower = (iter_num-2)**2 + 1
    a_max = (iter_num-1)//2
    right_upper_corner = lower + iter_num - 2
    left_upper_corner = right_upper_corner + iter_num - 1
    left_lower_corner = left_upper_corner + iter_num - 1
    right_lower_corner = left_lower_corner + iter_num - 1

    # print(num, lower, a_max, right_upper_corner, left_upper_corner, left_lower_corner, right_lower_corner)

    
    rem = num - lower
    if rem < iter_num - 1: # on the right side
        # print(num, 'right', lower, rem)
        a = a_max 
        b = -a_max + 1 + rem
        return a,b

    rem = num - right_upper_corner
    if rem  <= iter_num-1: # on the top
        # print(num, "top", left_lower_corner, rem)
        a = a_max - rem 
        b = a_max
        return (a,b)

    rem = num - left_upper_corner
    if rem  <= iter_num-1: # on the left
        a = -a_max
        b = a_max - rem
        return (a,b)

    rem = num - left_lower_corner
    if rem  <= iter_num-1: # on the bottom
        a = rem - a_max
        b = -a_max
        return (a,b)

    return 0,0


def man_dist(num): 
    a, b = spiral(num)
    # print(num, a, b)
    return abs(a) + abs(b)


def spiral_count(limit):

    num = 1

    s_num = 1

    spiral_vals = {(0,0):1}

    while num <= limit: 
        s_num += 1 

        a,b = spiral(s_num)

        v11  = spiral_vals.get((a+1,b+1),0)
        v10  = spiral_vals.get((a+1,b)  ,0)
        v1_1 = spiral_vals.get((a+1,b-1),0)
        v01  = spiral_vals.get((a  ,b+1),0)
        v0_1 = spiral_vals.get((a  ,b-1),0)
        v_11 = spiral_vals.get((a-1,b+1),0)
        v_10 = spiral_vals.get((a-1,b)  ,0)
        v_1_1= spiral_vals.get((a-1,b-1),0)


        num = v11 + v10 + v1_1 + v01 + v0_1 + v_11 + v_10 + v_1_1   
        spiral_vals[a,b] = num

    return num


if __name__ == "__main__": 

    # part 1 

    tests=[
        (1,0),
        (10,3), 
        (12,3), 
        (13, 4), 
        (14, 3), 
        (15, 2), 
        (16, 3), 
        (17, 4), 
        (18, 3), 
        (23, 2), 
        (25, 4), 
        (26, 5), 
        (48, 5),
        (1024, 31)
    ]

    # man_dist(14)
    # man_dist(15)
    # exit()
    for num, e_val in tests: 
        c_val = man_dist(num)
        print(num, c_val==e_val)

    print(312051, man_dist(312051))


    # part 2

    tests=[
        (10, 11), 
        (11, 23),
        (23, 25),
        (747, 806),
    ]

    print('\n\npart 2')
    for num, e_val in tests: 
        c_val = spiral_count(num)
        print(num, c_val == e_val)
    print('part 2 real', spiral_count(312051))
    
