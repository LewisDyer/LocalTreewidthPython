import networkx as nx

def parse_patents(filename):

    G = nx.Graph()

    with open(filename) as f:
        for line in f:
            if line.startswith('#'):
                continue
                
            to, fro = map(int, line.strip().split())
            G.add_edge(to, fro)
    
    print(nx.info(G))
    return G

if __name__ == '__main__':
    G = parse_patents("cit-Patents.txt")