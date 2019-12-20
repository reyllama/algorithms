def func(s):
    return func(s-1) + func(s-2) + func(s-3)

def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <= 3:
        return signature[:n]
    else:
        while len(signature) < n:
            signature.append(sum(signature[-3:]))
        return signature

print(tribonacci([3, 2, 1], 10))
