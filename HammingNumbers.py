import time

def is_hamming(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        return is_hamming(x/2)
    if x % 3 == 0:
        return is_hamming(x/3)
    if x % 5 == 0:
        return is_hamming(x/5)
    return 0

def hamming(n):
    i = 1
    k = 0
    while True:
        if is_hamming(i):
            k += 1
            if k == n:
                return i
        i +=1

def hamming(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        print("next_hamms: {}".format(next_hamms))
        next_hamm = min(next_hamms)
        print("next_hamm: {}".format(next_hamm))
        hamms.append(next_hamm)
        print("hamms: {}".format(hamms))
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)
        print("expos: {}".format(expos))
        print()
    return hamms[-1]



t0 = time.time()
print(hamming(10))
elapsed = time.time() - t0
print("It took %s seconds." % round(elapsed,2))
# print(is_hamming(35))
