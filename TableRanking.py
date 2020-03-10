def compute_ranks(number, games):
    d = dict()
    for i in range(number):
        d[i] = [0,0,0]
        for game in games:
            if i in game[:2]:
                pos = game[:2].index(i)
                pt = 2*(game[pos+2]>sum(game[-2:])/2) + (game[pos+2]==sum(game[-2:])/2)
                # print(game[pos+2], sum(game[-2:])/2)
                df = 2*(game[pos+2] - sum(game[-2:])/2)
                sc = game[pos+2]
                d[i] = [pt+d[i][0], df+d[i][1], sc+d[i][2]]
    X = sorted(d.items(), key=lambda e:e[1], reverse=True)
    r = dict()
    for i in range(len(X)):
        r[X[i][0]] = i+1
        if i>0:
            if X[i][1] == X[i-1][1]:
                r[X[i][0]] = r[X[i-1][0]]
    k = sorted(r.items())
    return [v for (t,v) in k]
    # return X
    # return d

def compute_ranks(number, games):
    ranks = []
    pts = [0] * number
    for game in games:
        if game[2] == game[3]:
            pts[game[0]] += 1
            pts[game[1]] += 1
            continue
        winner = game[max(zip(game[2:], range(2,4)))[1]-2]
        pts[winner] += 2
    if len(pts) == len(set(pts)):
        r = [(pt, sorted(pts, reverse=True).index(pt)) for pt in pts]
        return [v+1 for (t,v) in r]

    dfs = [0] * number
    for game in games:
        p1 = game[0]
        p2 = game[1]
        diff = game[2] - game[3]
        dfs[p1] += diff
        dfs[p2] -= diff
    gls = [0] * number
    for game in games:
        gls[game[0]] += game[2]
        gls[game[1]] += game[3]
    final = [1000*x+y+0.001*z for x,y,z in zip(pts, dfs, gls)]
    r = [(pt, sorted(final, reverse=True).index(pt)) for pt in final]
    # return final
    return [v+1 for (t,v) in r]


print(compute_ranks(6,
                [[0, 5, 2, 2],
                 [1, 4, 0, 2],
                 [2, 3, 1, 2],
                 [1, 5, 2, 2],
                 [2, 0, 1, 1],
                 [3, 4, 1, 1],
                 [2, 5, 0, 2],
                 [3, 1, 1, 1],
                 [4, 0, 2, 0]]))
# [4,4,6,3,1,2]
