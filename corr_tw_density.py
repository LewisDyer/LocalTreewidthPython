import matplotlib.pyplot as plt
import math

tws = []
densities = []
degrees = []
clusters = []
cores = []
with open("outputs/random_patents_tws.txt") as tw:
    for line in tw:
        tws.append(float(line.strip()))

with open("outputs/random_patents_density.txt") as dens:
    for line in dens:
        densities.append(float(line.strip()))

with open("outputs/random_patents_degrees.txt") as degs:
    for line in degs:
        degrees.append(int(line.strip()))

with open("outputs/random_patents_clustering.txt") as clus:
    for line in clus:
        clusters.append(float(line.strip()))

with open("outputs/random_patents_cores.txt") as cors:
    for line in cors:
        cores.append(int(line.strip()))
log_degrees = [math.log(d, 2) if d > 0 else 0 for d in degrees]


fig, ax = plt.subplots(5, figsize=(15,15))

fig.suptitle('Comparison between local density parameters for mico-like dataset')

ax[0].scatter(tws, densities, marker='.')
ax[0].set_xlabel("local treewidth")
ax[0].set_ylabel("local edge density")

ax[1].scatter(tws, degrees, marker='.')
ax[1].set_xlabel("local treewidth")
ax[1].set_ylabel("degree of starting vertex")

ax[2].scatter(degrees, densities, marker='.')
ax[2].set_xlabel("degree of starting vertex")
ax[2].set_ylabel("local edge density")

ax[3].scatter(densities, clusters, marker='.')
ax[3].set_xlabel("local edge density")
ax[3].set_ylabel("local clustering coefficient of starting vertex")

ax[4].scatter(tws, cores, marker='.')
ax[4].set_xlabel("local treewidth")
ax[4].set_ylabel("local degeneracy")

#sc = ax.scatter(tws, degrees,  marker='.')
plt.savefig('figures/random_patents_density.jpg', dpi=300)