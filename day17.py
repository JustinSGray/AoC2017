
def prob(step, stop, find): 

    buf = [0]
    cur_pos = 0
    for i in range(stop): 
        n_buf = len(buf)
        nex_pos = (cur_pos+step)%n_buf
        buf.insert(nex_pos+1, i+1)
        cur_pos = nex_pos+1
        # print(i, buf)
        if nex_pos == 0: 
            print(i+1)

    n_buf = len(buf)
    j = buf.index(find)

    return buf[(j+1)%n_buf]


def prob2(): 
    step = 344

    cur_pos = 0
    before_len = 0
    after_len = 0
    after_num = 0

    n_buf = 1

    for i in range(1, 50000001):
        cur_pos = ((cur_pos + step) % n_buf) + 1

        if cur_pos == (before_len + 1):
            after_num = i
            after_len += 1
        elif cur_pos > (before_len + 1):
            after_len += 1
        elif cur_pos < (before_len + 1):
            before_len += 1

        if i % 10000 == 0: 
            print(i)
        n_buf += 1

    return after_zero

#test
# print(prob(3, 2017, 2017))

# real1 
# print(prob(344, 2017, 2017))


print(prob(344, 50000, 0))


# real2
print(prob2())

# for i in range(1000000): 


