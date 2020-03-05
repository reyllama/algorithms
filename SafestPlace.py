def advice(agents, n):
    coors = [(i,j) for i in range(n) for j in range(n)]
    dist = dict()
    for coor in coors:
        dist[coor] = min([sum(coor-agent) for agent in agents])
    return dist[(2,2)]

################################################################################

def distance(co1, co2):
    return sum([abs(i-j) for i,j in zip(co1, co2)])

def advice(agents, n):
    coors = ((i,j) for i in range(n) for j in range(n))
    for agent in agents:
        if agent not in coors:
            agents.remove(agent)
    dist = {}
    for coor in coors:
        dist[coor] = min([distance(coor, agent) for agent in agents])
    ans = [k for k,v in dist.items() if (v == max(dist.values())) & (v>0)]
    return ans

###############################################################################

def advice(agents, n):
    coors = {(i,j) for i in range(n) for j in range(n)}
    if coors.issubset(set(agents)):
        return []
    elif len(agents) == 0:
        return coors
    sol = set()
    for coor in coors:
        d = min([distance(coor, agent) for agent in agents])
        if len(sol) < 1:
            sol.add((coor, d))
            continue
        o = sol.pop()
        if d > o[1]:
            sol.clear()
            sol.add((coor, d))
        elif d == o[1]:
            sol.update([o, (coor, d)])
        else:
            sol.add(o)
    ans = sorted([k for (k,v) in sol])
    return ans

###############################################################################

def advice(agents, n):
    frontier = {(x,y) for (x,y) in agents if 0<=x<n and 0<=y<n}
    bag = {(x,y) for x in range(n) for y in range(n)}
    if frontier == bag:
        return []
    while frontier and bag>frontier:
        bag -= frontier
        frontier = {pos for x,y in frontier for pos in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)) if pos in bag}
    return sorted(bag)

print(advice([(0,0), (0,2)], 2))
