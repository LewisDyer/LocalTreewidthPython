import networkx as nx
from collections import defaultdict
from pprint import pprint
import lg_parser
import patent_parser
import matplotlib.pyplot as plt


def degree_dist(G):
    degree_l = [val for (node, val) in G.degree()]

    degrees = defaultdict(int)
    for d in degree_l:
        degrees[d] += 1
    
    pprint(degrees)

    count = [0] * (max(degrees)+1)
    print(len(count))
    for key in degrees:
        #print("---")
        #print(key)
        print(f"{key} = {degrees[key]}")
        count[key] = degrees[key]

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(count)
    ax.set_yscale('log')
    plt.show()

if __name__ == '__main__':
    G = patent_parser.parse_patents("cit-Patents.txt")
    degree_dist(G)

    

