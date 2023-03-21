import matplotlib.pyplot as plt

tws = []
densities = []
with open("mico_tws.txt") as tw:
    for line in tw:
        tws.append(float(line.strip()))

with open("mico_density.txt") as dens:
    for line in dens:
        densities.append(float(line.strip()))


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.scatter(tws, densities, marker='.')
ax.set_xlabel("local treewidth")
ax.set_ylabel("local edge density")
plt.show()