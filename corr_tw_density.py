import matplotlib.pyplot as plt
import math

tws = []
densities = []
degrees = []
with open("outputs/mico_tws.txt") as tw:
    for line in tw:
        tws.append(float(line.strip()))

with open("outputs/mico_density.txt") as dens:
    for line in dens:
        densities.append(float(line.strip()))

with open("outputs/mico_degrees.txt") as degs:
    for line in degs:
        degrees.append(int(line.strip()))

log_degrees = [math.log(d, 2) if d > 0 else 0 for d in degrees]


fig, ax = plt.subplots(3, figsize=(15,15))

fig.suptitle('Comparison between local density parameters for mico dataset')

ax[0].scatter(tws, densities, marker='.')
ax[0].set_xlabel("local treewidth")
ax[0].set_ylabel("local edge density")

ax[1].scatter(tws, degrees, marker='.')
ax[1].set_xlabel("local treewidth")
ax[1].set_ylabel("degree of starting vertex")

ax[2].scatter(degrees, densities, marker='.')
ax[2].set_xlabel("degree of starting vertex")
ax[2].set_ylabel("local edge density")

#sc = ax.scatter(tws, degrees,  marker='.')
plt.savefig('figures/mico_density.png', dpi=300)