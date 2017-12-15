

class Gen(object): 

    def __init__(self, start, factor): 
        self.factor = factor

        self.last = start

    def __call__(self): 

        self.last = (self.last*self.factor)%2147483647

        return str(bin(self.last))[2:].rjust(32, '0')


def prob1(A_start, B_start): 
    gA = Gen(A_start, 16807)
    gB = Gen(B_start, 48271)

    count = 0
    for i in range(40*10**6): 
        count += gA()[16:] == gB()[16:]

    return count


# print('test1', prob1(65, 8921), 588)

# real 1 puzzle input A = 703, B = 516
# print('real1', prob1(703, 516))


class GenPicky(object): 

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
        return str(bin(self.last))[2:].rjust(32, '0')


def prob2(A_start, B_start): 
    gA = GenPicky(A_start, 16807, 4)
    gB = GenPicky(B_start, 48271, 8)

    count = 0
    for i in range(5*10**6): 
        a = gA()[16:]
        b = gB()[16:]
 
        count += a == b

    return count

# test
# print(prob2(65, 8921), 309)
#real
print(prob2(703, 516))