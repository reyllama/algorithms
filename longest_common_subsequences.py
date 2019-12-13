def lcs(x, y):
    if len(x) == 0 or len(y) == 0:
        return ""
    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1] # 재귀호출
    else:
        lcs1 = lcs(x[:-1], y)
        lcs2 = lcs(x, y[:-1])
        return lcs1 if len(lcs1)>=len(lcs2) else lcs2

print(lcs("BANANA", "ASTANA"))
