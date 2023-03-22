import matplotlib.pyplot as plt
from collections import defaultdict
from pprint import pprint

def read_tws_file(filename):
    tws = []
    with open(filename) as f:
        for line in f:
            tws.append(int(line))

    return tws

if __name__ == '__main__':
    tws = read_tws_file('patents_tws_degree.txt')
    #print(tws)

    counts = defaultdict(int)

    for tw in tws:
        counts[tw] += 1

    pprint(counts)

    count = [0] * (max(counts)+1)
    print(len(count))
    for key in counts:
        #print("---")
        #print(key)
        print(f"{key} = {counts[key]}")
        count[key] = counts[key]

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    #ax.plot(counts)
    ax.hist(tws, bins=100)
    ax.set_yscale('log')
    plt.show()

    print(count)
