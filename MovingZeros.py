def move_zeros(array):
    #your code here
    zeros = []
    for i in range(len(array)):
        if array[i] is False:
            continue
        elif array[i] == 0:
            zeros.append(i)
        else:
            continue
    for index in zeros[::-1]:
        del array[index]
    os = [0 for i in zeros]
    return array + os


def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

a = [9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]
b = [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
# print(sorted(a)==sorted(b))
# print(a.count(0))
# print(b.count(0))
# print(a.remove(0))
# print(sorted(a))
c = ["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]
# print(sorted(c))
print(move_zeros(c))
