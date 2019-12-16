def odd_row(n):
    return [k for k in range(n**2-n+1, n**2+n+1) if k % 2 == 1]

print(odd_row(10))
