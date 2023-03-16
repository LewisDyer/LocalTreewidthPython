import networkx as nx
import matplotlib.pyplot as plt

with open('mico_density_degree_remove_high_degree.txt') as f:
    lines = f.read().split('\n')[:-1]

lines = list(map(float, lines))

print(lines)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
#ax.plot(counts)
ax.hist(lines, bins=1000)
ax.set_yscale('log')
plt.show()