import networkx as nx
import lg_parser
import numpy as np
import matplotlib.pyplot as plt
def show_labels(G):
    # print sorted list of vertex and edge labels
    fields = set()
    for v in G.nodes():
        fields.add(G.nodes[v]['field'])
    
    print(fields)

    count = np.zeros((max(fields), max(fields)), dtype=int)

    for a, b in G.edges():
        field_a, field_b = G.nodes[a]['field'], G.nodes[b]['field']

        count[field_a-1][field_b-1] += 1
        if field_a != field_b:
            count[field_b-1][field_a-1] += 1

    print(count)

    count_norm = np.log10(count)

    fig, ax = plt.subplots(figsize=(20,20))

    im = ax.imshow(count_norm, interpolation='nearest')
    cbar = ax.figure.colorbar(im, ax=ax)

    row,col = count.shape
    for i in range(row):
        for j in range(col):
            if count[i,j] > 10000:
                text=ax.text(j, i, count[i, j], ha='center', va='center', color='w')
    plt.savefig('mico_matrix.jpg')
    plt.show()

    


if __name__ == '__main__':
    G = lg_parser.parse_lg("mico.lg")
    show_labels(G)