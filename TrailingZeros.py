def num(n, k):
    s = [i for i in range(n-(5**k-1), n+1) if i % 5**k == 0]
    return int(s[0]/5**k)

def zeros(n):
    import math
    s = 0
    if n <5:
        return 0
    for k in range(1, int(math.log(n, 5))+1):
        s += num(n, k)
    return s

print(zeros(126))
