def order_weight(strng):
    nums = strng.split()
    digits = []
    for num in nums:
        temp = [int(num[i]) for i in range(len(num))]
        digits.append(sum(temp))
    col = list(zip(digits, nums))
    X = " ".join([v for (k,v) in sorted(col)])
    return X


def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))

s1 = "2000 10003 1234000 44444444 9999 11 11 22 123"
print(order_weight(s1))

arr = [100, 150, 320, 220, 590, 419, 99, 51, 84]
arr = [str(num) for num in arr]
print(sorted(arr, key=lambda x: sum(int(c) for c in x)))
