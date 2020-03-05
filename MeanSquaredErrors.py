def solution(array_a, array_b):
    import numpy as np
    res = np.array(array_a) - np.array(array_b)
    return (sum([k**2 for k in res]))/len(res)

def solution(a, b):
    return sum([(a[i]-b[i])**2 for i in range(len(a))])/len(a)

b1 = [10, 20, 10, 2]
b2 = [10, 25, 5, -2]
print(solution(b1,b2))
