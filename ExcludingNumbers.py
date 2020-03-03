def removNb(n):
    ans = []
    import math
    for x in range(1, int(n/math.sqrt(2))+1):
        for y in range(int((n+1)/math.sqrt(2)), n):
            if x*y == n*(n+1)/2-(x+y):
                ans.append((x,y))
                ans.append((y,x))
    return sorted(ans)

def removNb(n):
    import math
    ans = []
    target = (n**2+n+2)/2
    for k in range(1, int(n/math.sqrt(2))+1):
        if target % k == 0:
            if target // k <= n:
                ans.append((k-1, int(target // k)-1))
                ans.append((int(target // k)-1, k-1))
    return sorted(ans)

def removNb(n):
    sol = []
    total = n*(n+1)/2
    for a in range(1, n+1):
        b = (total-a)/(a+1.0)
        if b.is_integer() and b <= n:
            sol.append((a,int(b)))
    return sol

print(removNb(26))
