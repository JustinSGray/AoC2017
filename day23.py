class Reg(object): 

    def __init__(self, instructions): 
        self.reg = [0]*8
        self.cur_location = 0

        self.lines = instructions.split("\n")

        self.num_mul = 0


    def part1(self): 

        while True: 

            try: 
                cmd = self.lines[self.cur_location].split()
            except IndexError: 
                break
            self.oper(cmd)

        return self.num_mul

    def oper(self, cmd): 
        inst = cmd[0]

        try: 
            target = int(cmd[1])
        except ValueError:
            target = ord(cmd[1])-97

        try: 
            val = int(cmd[2])
        except ValueError: 
            val = self.reg[ord(cmd[2])-97]

        # print(cmd, target, val)

        if inst == "set": 
            self.reg[target] = val
            
        elif inst == "sub": 
            self.reg[target] -=  val
            
        elif inst == "mul": 
            self.reg[target] *=  val
            self.num_mul += 1

        elif inst == "jnz": 
            if self.reg[target] != 0: 
                self.cur_location += val
                return 

        self.cur_location += 1


real="""set b 57
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23"""

reg = Reg(real)
print('part 1', reg.part1())


reg_b = 57 * 100 + 100_000  # puzzle_input[0], puzzle_input[4], puzzle_input[5]
reg_c = reg_b + 17_000  # puzzle_input[6], puzzle_input[7]
step_size = 17  # puzzle_input[30]

h = 0
for x in range(reg_b,reg_c+1,step_size):
    for i in range(2,x):
        if x % i == 0:
            h += 1
            break
print(h)