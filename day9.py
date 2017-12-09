class parser(object): 


    def __call__(self, line): 

        self.rank = 0
        self.in_garbage = False # if False, then we're in garbage
        self.ignore = False 

        self.points = []

        self.garbage_count = 0

        for char in line:
            self._inc(char)

        return self.points

    def _inc(self, char): 
        if self.ignore: 
            self.ignore = False 
            return 
        if char == "!": 
            self.ignore = True
            return 

        if self.in_garbage: 

            if char == ">": 
                self.in_garbage = False
                return 
            self.garbage_count += 1

        if not self.in_garbage: 
            if char == "<": 
                self.in_garbage = True
                return 
            
            
            if char == "{" : 
                self.rank += 1
                return 
            if char == "}" : 
                self.points.insert(0, self.rank)
                self.rank -= 1
                return 

if __name__ == "__main__": 

    test1_input = (
        ('{}', [1]), 
        ('{{{}}}', [1,2,3]), 
        ('{{},{}}', [1,2,2]),
        ('{{{},{},{{}}}}', [1,2,3,3,3,4]),
        ('{<a>,<a>,<a>,<a>}', [1]),
        ('{{<ab>},{<ab>},{<ab>},{<ab>}}', [1,2,2,2,2]), 
        ('{{<!!>},{<!!>},{<!!>},{<!!>}}', [1,2,2,2,2]), 
        ('{{<a!>},{<a!>},{<a!>},{<ab>}}', [1,2])
    )
    
    p = parser()
    for t in test1_input: 
        check = p(t[0])
        print(t[0], t[1], check)

    real_input = open('day9_input.txt').readline()
    p(real_input)
    print('real1', sum(p.points))
    print('real2', p.garbage_count)