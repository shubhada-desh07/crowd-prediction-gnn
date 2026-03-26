import torch
import numpy as np


def get_temple_graph(zone_counts):
    nodes = [
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"
    ]

    edges = [
        ("A","C"),
        ("B","D"),
        ("C","E"),
        ("C","F"),
        ("D","H"),
        ("E","F"),
        ("F","G"),
        ("H","I"),
        ("G","I"),
        ("I","J"),
        ("J","K"),
        ("J","L"),
        ("K","M"),
        ("L","M"),
        ("M","N"),
        ("N","A"),
        ("N","B")
    ]

    # Default values (from your graph)
    avg_flow = {
        "A":55, "B":42, "C":78, "D":24, "E":38,
        "F":62, "G":90, "H":22, "I":68, "J":95,
        "K":80, "L":45, "M":40, "N":55, "O":8
    }

    node_features = {}

    for node in nodes:
        count = zone_counts.get(node, 0)
        capacity = 100
        density = count / capacity

        node_features[node] = [count, avg_flow[node], density]

    x = np.array([node_features[n] for n in nodes])
    x = torch.tensor(x, dtype=torch.float)

    edge_index = []
    for e in edges:
        edge_index.append([nodes.index(e[0]), nodes.index(e[1])])

    edge_index = torch.tensor(edge_index).t().contiguous()

    return x, edge_index, nodes, node_features