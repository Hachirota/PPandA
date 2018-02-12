id = [0] * 10
for d in range(10):
    id[d] = d

def find(p):
    return id[p]

def connected(p,q):
    return id[p] == id[q]

def union(p,q):
    idp, idq = id[p], id[q]
    for i, e in enumerate(id):
        if id[i] == idp:
            id[i] = idq


