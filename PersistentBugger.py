def persistence(n):
    import numpy as np
    i = 0
    while n >= 10:
        digits = [int(str(n)[i]) for i in range(len(str(n)))]
        n = np.prod(digits)
        i += 1
    return i


print(persistence(999))
