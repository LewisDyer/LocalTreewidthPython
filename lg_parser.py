import networkx as nx
import matplotlib.pyplot as plt

def parse_lg(filename):

    G = nx.Graph()

    with open(filename) as f:
        for line in f:
            data = line.split(' ')

            token = data[0]
            if token == "v":
                v, label = int(data[1]), int(data[2])
                G.add_node(v, field=label)
            elif token == "e":
                u, v, label = int(data[1]), int(data[2]), int(data[3])
                G.add_edge(u, v, no_papers=label)

    return G

if __name__ == '__main__':
    G = parse_lg("mico.lg")
