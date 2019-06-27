def list_squared(m, n):
    squared = []
    for k in range(m, n):
        divisors = [i**2 for i in range(1, k+1) if k % i == 0]
        num = sum(divisors)
        if (num**0.5).is_integer():
            squared.append([k, num])
    return squared


### Working Answer on Optimization

# CACHE = {}
#
# def squared_cache(number):
#     if number not in CACHE:
#         divisors = [x for x in range(1, number + 1) if number % x == 0]
#         CACHE[number] = sum([x * x for x in divisors])
#         return CACHE[number]
#
#     return CACHE[number]
#
# def list_squared(m, n):
#     ret = []
#
#     for number in range(m, n + 1):
#         divisors_sum = squared_cache(number)
#         if (divisors_sum ** 0.5).is_integer():
#             ret.append([number, divisors_sum])
#
#     return ret
#
# print(list_squared(2, 51000))
