# un = (1/n!) * (1! + 2! + 3! + ... + n!)
## result truncated at 6 decimal point

def factorial(k):
    if k == 1:
        return 1
    return k*factorial(k-1)

def sub_fac(n, k):
    if k == 0:
        return n
    return (n-k)*sub_fac(n, k-1)

def going(n):
    if n > 100:
        temp = sum([(1/sub_fac(n, k)) for k in range(0, 21)])+1
    else:
        temp = 1/factorial(n) * sum([factorial(k) for k in range(1, n+1)])
    return float(str(temp)[:8])
    # return temp
    # your code

# print(factorial(9))
print(going(2000))
# print(1/factorial(10))

# print(sub_fac(6, 0))
