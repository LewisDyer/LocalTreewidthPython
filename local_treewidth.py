import networkx as nx
from networkx.algorithms.approximation import treewidth_min_degree
import matplotlib.pyplot as plt
import multiprocessing as mp

import lg_parser
import patent_parser

def local_treewidth(G, radius):

    treewidths = [0] * len(G.nodes())
    densities = [0] * len(G.nodes())
    degrees = [0] * len(G.nodes())
    clustering = [0] * len(G.nodes())

    clusters = nx.clustering(G)
    for i, v in enumerate(G.nodes()):

        ball = nx.ego_graph(G, v, radius)
        tw = treewidth_min_degree(ball)[0]
        treewidths[i] = tw
        densities[i] = nx.density(ball)
        degrees[i] = G.degree(v)
        clustering[i] = clusters[v]
        if i % 1000 == 0:
            print(i)
    
    return(treewidths, densities, degrees, clustering)
    # for vertex in G:
    # get ball of defined radius around vertex
    # find treewidth of this ball
    # just print out result for now

if __name__ == '__main__':
    #G = nx.erdos_renyi_graph(100, 0.025)

    #nx.draw(G)
    #plt.show()
    G = lg_parser.parse_lg('datasets/mico.lg')
    #G = patent_parser.parse_patents('datasets/cit-Patents.txt')
    tws, dens, degs, clus = local_treewidth(G, 1)
    f = open("outputs/mico_tws.txt", "w")
    for tw in tws:
        f.write(f"{tw}\n")
    f = open("outputs/mico_density.txt", "w")
    for den in dens:
        f.write(f"{den}\n")
    f = open("outputs/mico_degrees.txt", "w")
    for deg in degs:
        f.write(f"{deg}\n")
    
    f = open("outputs/mico_clustering.txt", "w")
    for clu in clus:
        f.write(f"{clu}\n")
    
    f.close()
    