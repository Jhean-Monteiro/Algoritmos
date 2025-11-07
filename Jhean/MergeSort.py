def merge_sort(a):
    if len(a) <= 1: return a

    m = len(a)//2
    return merge(merge_sort(a[:m]), merge_sort(a[m:]))

def merge(e, d):
    r, i, j = [], 0, 0

    while i < len(e) and j < len(d):
        if e[i] <= d[j]: 
            r.append(e[i]); i += 1
        else: 
            r.append(d[j]); j += 1
    return r + e[i:] + d[j:]

print(merge_sort([64,34,25,12,22,11,90]))