from algopy import graph, stack


def pondere_simple(G):
    cc = 0
    IC2 = 0
    M = [False] * G.order
    for i in range(G.order):
        if not M[i]:
            cc += 1
            nb = __dfs(G, i, M)
            IC2 += nb**2
    return (G.order - cc)/(G.order-1), IC2 / G.order**2


def __dfs(G, x, M):
    M[x] = True
    no = 0
    for adj in G.adjlists[x]:
        if not M[adj]:
            no = __dfs(G, adj, M) + 1
    return no
