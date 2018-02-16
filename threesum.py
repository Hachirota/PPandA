class threesum:
    def __init__(self, *args):
        self.input = args
        self.lt = list(self.input)


    def evaluate(self):
        self.lt.sort()
        n = len(self.lt)
        count = 0
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if self.lt[i] + self.lt[j] + self.lt[k] == 0:
                        count += 1
        return count
