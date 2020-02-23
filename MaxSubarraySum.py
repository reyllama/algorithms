def max_sequence(arr):
    max = 0
    for num in arr:
        print("num: ", num)
        if max + num > 0:
            max += num
        else:
            max = 0
        print("max: ", max)
    return max

def max_sequence(arr):
    maxi = 0
    memo = set()
    memo.add(maxi)
    for num in arr:
        if maxi + num > 0:
            memo.add(maxi+num)
            maxi += num
        else:
            maxi = 0
    return max(memo)


l1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_sequence(l1))
