# 주어진 array 내의 원소들을 이용한 모든 순열 만들기
def exhaustive_permutation(arr, ans=[], ret=[]):
    if len(arr) == 0:
        ret.append(ans)
    for i, c in enumerate(arr):
        tmp = arr[:i] + arr[i+1:]
        exhaustive_permutation(tmp, ans+[c])
    return ret

# 주어진 원소 중 r개를 사용하는 모든 조합 만들기
def exhaustive_combination(arr, r, ans=[], ret=[]):
    if r == 0:
        ret.append(ans)
        return
    for i, c in enumerate(arr):
        tmp = arr[i+1:]
        exhaustive_combination(tmp, r-1, ans+[c])
    return ret

