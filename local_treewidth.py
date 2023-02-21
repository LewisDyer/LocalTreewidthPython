import networkx as nx
from networkx.algorithms.approximation import treewidth_min_degree
import matplotlib.pyplot as plt

import lg_parser

def local_treewidth(G, radius):

    treewidths = [0] * len(G.nodes())
    for i, v in enumerate(G.nodes()):
        ball = nx.ego_graph(G, v, radius)
        tw = treewidth_min_degree(ball)[0]
        treewidths[i] = tw

        if i % 1000 == 0:
            print(i)
        #print(tw)
    
    return(treewidths)
    # for vertex in G:
    # get ball of defined radius around vertex
    # find treewidth of this ball
    # just print out result for now

if __name__ == '__main__':
    #G = nx.erdos_renyi_graph(100, 0.025)

    #nx.draw(G)
    #plt.show()
    G = lg_parser.parse_lg("mico.lg")
    tws = local_treewidth(G, 1)
    f = open("tws.txt", "w")
    for tw in tws:
        f.write(f"{tw}\n")
    
    f.close()
    