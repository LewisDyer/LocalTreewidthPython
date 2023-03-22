import matplotlib.pyplot as plt
import math

tws = []
densities = []
degrees = []
with open("outputs/patents_tws.txt") as tw:
    for line in tw:
        tws.append(float(line.strip()))

with open("outputs/patents_density.txt") as dens:
    for line in dens:
        densities.append(float(line.strip()))

with open("outputs/patents_degrees.txt") as degs:
    for line in degs:
        degrees.append(int(line.strip()))

log_degrees = [math.log(d, 2) if d > 0 else 0 for d in degrees]


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

sc = ax.scatter(tws, densities, marker='.', c=degrees, cmap=plt.cm.Blues)
cbar = plt.colorbar(sc)
# ax.set_xlabel("local treewidth")
# ax.set_ylabel("local edge density")
# plt.show()

#sc = ax.scatter(tws, degrees,  marker='.')
plt.show()