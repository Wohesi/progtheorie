import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


class visualisation:

    def distribution(countryList):
        # changeable values
        colourmap =  ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        barwidth = 0.25 # width of individual bars

        # generated values
        N = 0           # amount of frequencies
        x = []          # list of frequencies
        y = []          # list of frequency amount lists per country

        # this loop checks which of the graphs has the most frequencies
        # and adds each distribution to the y-list
        for g in countryList:
            freqcounts = Counter(list(nx.get_node_attributes(g.cg, 'freq').values()))

            radioFrequencies = freqcounts.keys()
            if len(radioFrequencies) > N:
                N = len(radioFrequencies)
                x = list(radioFrequencies)
            y.append(list(freqcounts.values()))

        # arange the values according to the highest amount of frequencies
        ind = np.arange(N)


        # pad the list with extra 0's for frequencies that don't exist
        # in some lists
        for l in y:
            if len(l) < N:
                l.extend([0] * (N - len(l))) # extend the missing amount


        ax = plt.subplot(111)

        # set up bars for each country
        for i,g in enumerate(y):
            ax.bar( ind + (i * barwidth),
                    g,
                    barwidth,
                    align='center',
                    color=colourmap[i])

        ax.set_xticks(ind + barwidth)
        ax.set_xticklabels([x+1 for x in ind])

        ax.set_ylabel("Frequency Amount")

        plt.show()
