import networkx as nx
from networkx.algorithms.approximation import treewidth_min_degree
import matplotlib.pyplot as plt
import multiprocessing as mp

import lg_parser
import patent_parser

def process_local(G, i, v, radius, tws, dens, degs):
    ball = nx.ego_graph(G, v, radius)
    tw = treewidth_min_degree(ball)[0]
    tws[i] = tw
    dens[i] = nx.density(ball)
    degs[i] = G.degree(v)
    if i % 10 == 0:
        print(i)

def local_treewidth(G, radius):

    treewidths = [0] * len(G.nodes())
    densities = [0] * len(G.nodes())
    degrees = [0] * len(G.nodes())
    for i, v in enumerate(G.nodes()):

        process = mp.Process(target=process_local, args=(G,i,v,radius,treewidths,densities,degrees))
        process.start()
        process.join(timeout=1)

        if process.is_alive():
            process.terminate()
            process.join()
            print(f"timeout at i={i}")
    
    return(treewidths, densities, degrees)
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
    tws, dens, degs = local_treewidth(G, 2)
    f = open("outputs/mico2_tws.txt", "w")
    for tw in tws:
        f.write(f"{tw}\n")
    f = open("outputs/mico2_density.txt", "w")
    for den in dens:
        f.write(f"{den}\n")
    f = open("outputs/mico2_degrees.txt", "w")
    for deg in degs:
        f.write(f"{deg}\n")

    
    f.close()
    