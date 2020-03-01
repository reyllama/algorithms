## x**2 - 4y**2 = n
## (x-2y)(x+2y) = n
## x > 2y
## x + 2y <= n
## x > sqrt(n)
## x**2 -n = 4*y**2 = (2y)**2
## 제곱수의 성질


def sol_equa(n):
    import math
    sol = []
    for x in range(int(math.sqrt(n)), n):
        k = (x**2 - n)
        if (k % 4 == 0) and (k % 10 in (0,4,6)):
            for y in range(0, int(x/2)+1):
                if (2*y)**2 == k:
                    sol.append([x,y])
    return sol

def sol_equa(n):
    import math
    sol = []
    for x in range(1, int(math.sqrt(n))+1):
        if n % x == 0:
            y = n // x
            if (y-x) % 4 == 0:
                sol.append([int((x+y)/2), int((y-x)/4)])
    return sol


print(sol_equa(100))
