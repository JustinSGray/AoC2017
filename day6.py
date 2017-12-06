import numpy as np 

def redistribute(input): 
    banks = [int(s) for s in input.split()]
    n_banks = len(banks)

    i_max = np.argmax(banks)

    blocks = banks[i_max]

    banks[i_max] = 0 

    for i in range(i_max+1, i_max+blocks+1): 
        i_circ = i % n_banks
        banks[i_circ] += 1

    return " ".join([str(x) for x in banks])

def redistribute_loop(input): 

    seen = []
    while input not in seen: 
        seen.append(input)
        input = redistribute(input)

    i_match = seen.index(input)
    l_seen = len(seen)
    return l_seen, l_seen - i_match 



if __name__ == "__main__": 


    test1_input ="""0 2 7 0""" 
    e_val = "2 4 1 2"
    c_val = redistribute(test1_input)
    print('test1 check1 redistribute', c_val == e_val)

    e_val = "3 1 2 3"
    c_val = redistribute(c_val)
    print('test1 check2 redistribute', c_val == e_val)

    e_val = "0 2 3 4"
    c_val = redistribute(c_val)
    print('test1 check3 redistribute', c_val == e_val)

    e_val = "1 3 4 1"
    c_val = redistribute(c_val)
    print('test1 check4 redistribute', c_val == e_val)

    e_val = "2 4 1 2"
    c_val = redistribute(c_val)
    print('test1 check5 redistribute', c_val == e_val)

    print('test1 check loop', redistribute_loop(test1_input)[0] == 5 )

    real_input = """4   10  4   1   8   4   9   14  5   1   14  15  0   15  3   5"""
    # real_input = " ".join(real_input.split())
    # print("real 1", redistribute_loop(real_input))

    test2_input ="""2 4 1 2"""
    print('test2 check', redistribute_loop(test2_input)[1] == 4)

    print('test2 real', redistribute_loop(real_input)[1])
