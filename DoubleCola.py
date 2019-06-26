def who_is_next(names, r):
    le = len(names)
    for n in range(200):
        if le*(2**(n+1)-1)>r:
            next = le*(2**(n+1)-1)
            group = le*(2**n-1)
            for i in range(le):
                if r in range(group+int(i*(next-group)/le)+1, group+int((i+1)*(next-group)/le)+1):
                    return names[i]
                    break
            break

# def whoIsNext(names, r):
#     while r > 5:
#         r = (r - 4) / 2
#     return names[r-1]
# Respect!!
