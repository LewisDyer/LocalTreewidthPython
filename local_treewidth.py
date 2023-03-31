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
    cores = [0] * len(G.nodes())

    clusters = nx.clustering(G)
    for i, v in enumerate(G.nodes()):

        ball = nx.ego_graph(G, v, radius)
        tw = treewidth_min_degree(ball)[0]
        treewidths[i] = tw
        densities[i] = nx.density(ball)
        degrees[i] = ball.degree(v)
        clustering[i] = clusters[v]
        clear_ball = ball.remove_edges_from(nx.selfloop_edges(ball))
        if clear_ball is not None:
            cores[i] = min(nx.core_number(clear_ball).values())
        if i % 1000 == 0:
            print(i)
    
    return(treewidths, densities, degrees, clustering, cores)
    # for vertex in G:
    # get ball of defined radius around vertex
    # find treewidth of this ball
    # just print out result for now

if __name__ == '__main__':
    #G = nx.erdos_renyi_graph(100, 0.025)

    #nx.draw(G)
    #plt.show()
    #G = lg_parser.parse_lg('datasets/mico.lg')
    #G = patent_parser.parse_patents('datasets/cit-Patents.txt')
    #G = nx.gnm_random_graph(100000,1080156) # mico like
    G = nx.gnm_random_graph(3774768, 16518948) # patents like
    tws, dens, degs, clus, cores = local_treewidth(G, 1)
    f = open("outputs/random_patents_tws.txt", "w")
    for tw in tws:
        f.write(f"{tw}\n")
    f = open("outputs/random_patents_density.txt", "w")
    for den in dens:
        f.write(f"{den}\n")
    f = open("outputs/random_patents_degrees.txt", "w")
    for deg in degs:
        f.write(f"{deg}\n")
    
    f = open("outputs/random_patents_clustering.txt", "w")
    for clu in clus:
        f.write(f"{clu}\n")

    f = open("outputs/random_patents_cores.txt", "w")
    for cor in cores:
        f.write(f"{cor}\n")

    
    f.close()
    