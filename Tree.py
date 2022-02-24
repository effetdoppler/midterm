from algopy import graph


def tree(G):
    cc = [None] * G.order
    __make(G, 0, -1, cc, 1)
    x = 0
    c = 1
    for i in range(1, G.order):
        if cc[i] is None:
            c += 1
            __make(G, i, -1, cc, c)
            G.addedge(x, i)
    return cc


def __make(G, x, p, cc, no):
    cc[x] = no
    for adj in G.adjlists[x]:
        if cc[adj] is not None:
            __make(G, adj, x, cc, no)
        elif adj != p:
            G.removeefge(adj, p)
            