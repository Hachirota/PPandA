def merge(a1, a2, a):
    i = j = 0
    while i + j < len(a):
        if j == len(a2) or (i < len(a1) and a1[i] < a2[j]):
            a[i+j] = a1[i]
            i += 1
        else:
            a[i+j] = a2[j]
            j += 1
