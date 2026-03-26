import torch
import numpy as np


def get_bus_graph(zone_counts):
    nodes = ["A","B","C","D","E","F","G"]

    edges = [
        ("A","C"),
        ("B","C"),
        ("C","F"),
        ("C","G"),
        ("D","F"),
        ("D","G"),
        ("E","A"),
        ("C","D"),
        ("F","G")
    ]

    avg_flow = {
        "A":32, "B":18, "C":48, "D":29,
        "E":6, "F":38, "G":34
    }

    node_features = {}

    for node in nodes:
        count = zone_counts.get(node, 0)
        capacity = 80
        density = count / capacity

        node_features[node] = [count, avg_flow[node], density]

    x = np.array([node_features[n] for n in nodes])
    x = torch.tensor(x, dtype=torch.float)

    edge_index = []
    for e in edges:
        edge_index.append([nodes.index(e[0]), nodes.index(e[1])])

    edge_index = torch.tensor(edge_index).t().contiguous()

    return x, edge_index, nodes, node_features