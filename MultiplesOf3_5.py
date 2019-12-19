def solution(number):
    return sum(set([k for k in range(1, number) if (k % 3 == 0) | (k % 5 == 0)]))

print(solution(10))
