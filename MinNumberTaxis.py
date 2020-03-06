# First working solution
def min_num_taxis(requests):
    n = 0
    requests = sorted(requests)
    while requests:
        n += 1
        v = requests[0][1]
        del requests[0]
        for x,y in requests:
            if x > v:
                v = y
                requests.remove((x,y))
    return n

###############################################################################

# def min_num_taxis(requests):
#     n = 0
#     while requests:
#         v = min(requests)[1]
#         for i in range(1, 10000):
#             if requests.find((v+i, )):
#                 requests.remove(requests[requests.find((v+i,))])

def min_num_taxis(requests):
    import numpy as np
    x = np.zeros(max(y for _,y in requests)+1)
    for i,j in requests:
        x[i:j+1] += 1
    return x.max()


three_reqs = [(1,4), (2, 9), (3, 6)] # Three requests, three taxis.
four_reqs = [(1,4), (2, 9), (3, 6), (5, 8)] # Four requests, three taxis.

print(min_num_taxis(four_reqs))
# print(min(four_reqs))
# print(four_reqs.find((2,)))
# print(four_reqs.count((2, )))
