import networkx as nx
import matplotlib.pyplot as plt
import analysis.lg_parser as lg_parser
import analysis.patent_parser as patent_parser

def degeneracy(G):
    core_values = nx.core_number(G)
    #print(core_values.values())
    return (core_values.values(), max(core_values.values()))

if __name__ == '__main__':
    #G = lg_parser.parse_lg('mico.lg')
    G = patent_parser.parse_patents('cit-Patents.txt')
    G.remove_edges_from(nx.selfloop_edges(G))
    core, deg = degeneracy(G)
    print(f"graph has degeneracy {deg}")

    print(core)


    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    #ax.plot(counts)
    ax.hist(core, bins=max(core))
    ax.set_yscale('log')
    plt.show()