id = [0] * 10
for d in range(10):
    id[d] = d

def find(p):
    while id[p] != p:
        p = id[p]
    return p

def connected (p,q):
    return find(p) == find(q)

def union(p,q):
    a = find(p)
    b = find(q)
    id[a] = id[b]

union(2,3)
union(2,4)
union(9,6)
union(2,9)

print(id)