def interleave(*args):
    max_length = max([len(arg) for arg in args])
    for arg in args:
        arg += (max_length-len(arg))*[None]
    ans = []
    for i in range(max_length):
        ans += [arg[i] for arg in args]
    return ans


# interleave([1, 2, 3], [4, 5])
# [1, 4, 2, 5, 3, None]

print(interleave([1,2,3,4], [2,2], [3,1,1,1,1,1], [0,3,4]))
