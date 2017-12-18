test1 = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

test2="""snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""


real = """set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 735
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19"""



class Reg(object): 

    def __init__(self, instructions): 
        self.reg = [0]*26
        self.cur_location = 0

        self.lines = instructions.split("\n")

        self.last_played = 0 
        self.last_heard = 0


    def part1(self): 

        while True: 
            cmd = self.lines[self.cur_location].split()
            self.oper(cmd)
            if self.last_heard: 
                break 

        return self.last_heard

    def oper(self, cmd): 
        inst = cmd[0]
        target = ord(cmd[1]) - 97
    
        # print(cmd)

        if inst == "snd": 
            self.last_played = self.reg[target]
            self.cur_location += 1  
            # print(self.cur_location, "snd", last_played)
            return
        elif inst == "rcv": 
            if self.reg[target] != 0: 
                self.last_heard = self.last_played
                # print('rcv', last_heard)
            else: 
                self.cur_location += 1
            return 
        try: 
            val = int(cmd[2])
        except ValueError: 
            val = self.reg[ord(cmd[2])-97]

        if inst == "set": 
            self.reg[target] = val
            
        elif inst == "add": 
            self.reg[target] +=  val
            
        elif inst == "mul": 
            self.reg[target] *=  val
            
        elif inst == "mod": 
            self.reg[target] = self.reg[target] %  val
            
        elif inst == "jgz": 
            if self.reg[target] != 0: 
                self.cur_location += val
                return 
        self.cur_location += 1


class Reg2(object): 

    def __init__(self, id): 
        self.reg = [0]*26
        self.cur_location = 0

        self.last_played = 0 
        self.last_heard = 0

        self.snd_counter = 0

        self.reg[ord('p') - 97] = id
        self.id = id

        self.queue = []

        self.wait = False
        self.stop = False

    def send_to_pair(self, val): 
        self.pair.queue.append(val)
        self.pair.wait = False

    def oper(self, cmd): 
        inst = cmd[0]
        try: 
            target = int(cmd[1])
        except ValueError: 
            target = ord(cmd[1]) - 97

    
        # print(self.id, cmd)
        if inst == "snd": 
            try: 
                val = int(cmd[1])
            except ValueError: 
                val = self.reg[ord(cmd[1])-97]
            self.send_to_pair(val)
            # print(self.id, "snd", val, len(self.pair.queue))
            self.snd_counter += 1
            self.cur_location += 1 
            return 

        elif inst == "rcv":
            try: 
                val = int(cmd[1])
            except ValueError: 
                val = ord(cmd[1])-97 
        
            if self.queue: 
               
                # print(self.id, 'rcv', cmd, val)
                self.reg[val] = self.queue.pop(0)
                self.cur_location += 1
            elif self.reg[val] !=0: 
                self.stop = True
            else: 
                self.wait = True
            return 

        try: 
            val = int(cmd[2])
        except ValueError: 
            val = self.reg[ord(cmd[2])-97]

        if inst == "set": 
            self.reg[target] = val
            
        elif inst == "add": 
            self.reg[target] +=  val
            
        elif inst == "mul": 
            self.reg[target] *=  val
            
        elif inst == "mod": 
            self.reg[target] = self.reg[target] %  val
            
        elif inst == "jgz": 
            if self.reg[target] > 0: 
                self.cur_location += val
                return 
        self.cur_location += 1


# reg = Reg(test1)
# print(reg.part1())

import time 
st = time.time()

reg = Reg(real)
print('part 1', reg.part1())


rega = Reg2(0)
regb = Reg2(1)



rega.pair = regb
regb.pair = rega


lines = real.split("\n") 
n_lines = len(lines)
while not ((rega.wait or rega.stop) and (regb.wait or regb.stop)): 

    cmd_a = lines[rega.cur_location].split()
    rega.oper(cmd_a)


    cmd_b = lines[regb.cur_location].split()
    regb.oper(cmd_b)



print('part 2', regb.snd_counter)
print('time', time.time() - st)


