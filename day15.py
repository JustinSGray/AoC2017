


bit_mask = 0b1111111111111111

class Gen(object): 

    def __init__(self, start, factor, lcm): 
        self.factor = factor

        self.last = start

        self.lcm = lcm

    def __call__(self): 

        while True: 
            self.last = (self.last*self.factor)%2147483647
            if self.last % self.lcm == 0: 
                break

        # return self.last
        return self.last

def prob(A_start, B_start, lcm_A=1, lcm_B=1, n_pairs=40*10**6): 
    gA = Gen(A_start, 16807, lcm_A)
    gB = Gen(B_start, 48271, lcm_B)

    count = 0
    for i in range(n_pairs): 
        count += gA() & bit_mask == gB() & bit_mask

    return count


# print('test1', prob(65, 8921), 588)

# real 1 puzzle input A = 703, B = 516
# print('real1', prob(703, 516))

# test
# print(prob2(65, 8921, 4, 8, 5*10**6), 309)
#real


import time 
st = time.time()
print(prob(703, 516, 4, 8, 5*10**6))

print('time {} seconds'.format(time.time() - st))