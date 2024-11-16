def devoir1(trajets_train, durees_train, ville_depart, durees_voldirect, sacrifice):
    import numpy as np

    class Graph:
        def __init__(self, nodes: list[str], edges: set[tuple]) -> None:
            self.nodes = nodes
            self.edges = edges

    G = Graph([], set([]))

    # UNPACK GRAPH DATA INTO "G"
    for traj, cost in zip(trajets_train, durees_train):
        node1, node2 = traj.split("-")
        if node1 not in G.nodes:
            G.nodes.append(node1)
        if node2 not in G.nodes:
            G.nodes.append(node2)

        G.edges.add((node1, node2, cost + 15))

    G.nodes = sorted(G.nodes)

    # BELLMAN-FORD
    distances = dict(zip(G.nodes, np.full(len(G.nodes), np.inf)))
    distances[ville_depart] = 0
    for _ in range(len(G.nodes) - 1):
        for arete in G.edges:
            s, t, c = arete
            if distances[t] > distances[s] + c:
                distances[t] = distances[s] + c
            if distances[s] > distances[t] + c:
                distances[s] = distances[t] + c
    del distances[ville_depart]

    # CORRECTION AVEC TEMPS DE TRANSFERT/ATTENTE
    min_distances_train = np.array(list(distances.values())) + 15
    min_distances_avion = np.array(durees_voldirect) + 180

    count_train = (min_distances_train <= min_distances_avion + sacrifice).sum()
    ville = G.nodes
    ville.remove(ville_depart)
    return ville, min_distances_train, min_distances_avion, count_train
