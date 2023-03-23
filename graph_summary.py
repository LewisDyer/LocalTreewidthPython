import networkx as nx
import lg_parser
import patent_parser

# given a graph G, output a report summarising a bunch of information about that graph.

def summarise(G, graph_name):
    f = open(f"outputs/report_{graph_name}.txt", "w")

    f.write(f"REPORT for {graph_name} graph:\n")

    f.write(f"{G.number_of_nodes()} nodes\n")

    f.write(f"{G.number_of_edges()} edges\n")

    f.write(f"Average degree is {G.number_of_edges()/G.number_of_nodes()}\n")



    f.close()


if __name__ == '__main__':
    #G = lg_parser.parse_lg('datasets/mico.lg')
    G = patent_parser.parse_patents('datasets/cit-Patents.txt')
    summarise(G, 'patents')