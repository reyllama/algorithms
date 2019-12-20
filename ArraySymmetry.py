def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    else:
        return -1
#
# def find_even_index(arr):
#     for i in range(len(arr)):
#         return i if sum(arr[:i]) == 0.5*sum(arr) else -1

print(find_even_index([10,-80,10,10,15,35,20]))
