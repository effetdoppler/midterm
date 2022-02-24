from algopy import graph

def condensation(G, scc):
    scccomp = [None] * G.order
    length = len(scc)
    for i in range(length):
        for comp in scc[i]:
            scccomp[comp] = i
    G1 = graph.Graph(G.order, True)
    for i in range(G.order):
        for adj in G.adjlists[i]:
            if scc[i] != scc[adj] and scc[adj] not in G1.adjlists[scc[i]]:
                G.addedge(i, adj)
    return G1

