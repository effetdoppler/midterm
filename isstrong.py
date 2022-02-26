from algopy import graph


def is_strong(G):
    cpt = 0
    pref = [None] * G.order
    return_x, cpt = __istrong(G, 0, pref, cpt)
    return cpt == G.order


def __istrong(G, x, pref, cpt):
    cpt += 1
    pref[x] = cpt
    return_x = pref[x]
    for adj in G.adjlists[x]:
        if pref[adj] is None:
            return_y, cpt = __istrong(G, adj, pref, cpt)
            if return_y == -1:
                return -1, cpt
            return_x = min(return_y, return_x)
        else:
            return_x = min(return_x, pref[adj])
    if return_x == pref[x]:
        if pref[x] != -1:
            return -1, cpt
    return return_x, cpt
