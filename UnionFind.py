class UnionFind:
    def __init__(self, n):
        self.id = list(range(n))
        self.lr = [1] * n

    def findroot(self, p):
        a = p
        while a != self.id[a]:
            self.id[a] = self.id[self.id[a]]
            a = self.id[a]
        return a

    def connected(self, p, q):
        return self.findroot(p) == self.findroot(q)

    def union(self, p, q):
        i = self.findroot(p)
        j = self.findroot(q)
        if i == j:
            return
        if (self.lr[i] < self.lr[j]):
            self.id[i] = j
            self.lr[j] += self.lr[i]
        else:
            self.id[j] = i
            self.lr[i] += self.lr[j]


