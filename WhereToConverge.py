## Codewars Kata "Which X for that sum?"

import math

def solve(m):
    import math
    return math.exp(-math.sqrt(1/m))
    # your code

def solve(m):
    import math
    return (2*m+1-math.sqrt(4*m+1))/(2*m)

# print(0.99**300)
print(solve(2))
print(solve(4))
print(solve(5))
# print(math.exp(math.sqrt(1/2)))
# n = 1000000
# print(n*(99/100)**n)
