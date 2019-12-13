def choose_best_sum(t, k, ls):
    for x in ls:
        return choose_best_sum(t-x, k-1, ls-list(x))

arr = [5, 9, 7, 3, 2]
