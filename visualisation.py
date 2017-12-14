import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


class visualisation:

    def distribution(countryList):
        # changeable values
        colourmap =  ['royalblue', 'orange', 'limegreen', 'hotpink',
                    'red', 'cyan', 'yellow']
        barwidth = 0.3 # width of individual bars

        # generated values
        N = 0           # amount of frequencies
        x = []          # list of frequencies
        y = []          # list of frequency amount lists per country
        a = []          # list of algorithm types (index must be equal to y)

        # this loop checks which of the graphs has the most frequencies
        # and adds each distribution to the y-list
        for c in countryList:
            freqcounts = Counter(list(nx.get_node_attributes(c.cg, 'freq').values()))

            radioFrequencies = freqcounts.keys()
            if len(radioFrequencies) > N:
                N = len(radioFrequencies)
                x = list(radioFrequencies)
            y.append(list(freqcounts.values()))
            a.append(c.algorithmType)

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
                    color=colourmap[i],
                    label=a[i])

        ax.set_xticks(ind + barwidth)
        ax.set_xticklabels([x+1 for x in ind])

        ax.set_ylabel("Frequency Amount")
        ax.set_xlabel("Frequency Type")
        ax.legend()
        # ax.title("The frequency distribution in %c" %countryList[0].countryName)

        plt.show()

    def visualisation(country):

        # the available colours that can be used to colour in the graph
        c = {1: 'royalblue', 2: 'orange', 3: 'limegreen', 4: 'hotpink',
             5: 'red', 6: 'cyan', 7: 'yellow'}

        freqDict = nx.get_node_attributes(country.cg, 'freq')
        colorDict = {node: c[freqDict[node]] for node in freqDict}
        colors = list(zip(colorDict, colorDict.values()))

        nx.spring_layout(country.cg)

        plt.figure(figsize=(15,15))

        pos = nx.spring_layout(country.cg)
        nx.draw_networkx_nodes(country.cg, pos,
                                nodelist=[x[0] for x in colors],
                                node_color=[x[1] for x in colors],
                                node_size=600,
                                alpha=0.8)
        nx.draw_networkx_labels(country.cg, pos,
                                nodelist=country.cg.nodes(),
                                font_size=12)
        nx.draw_networkx_edges(country.cg, pos,
                                edgelist=country.cg.edges(),
                                edge_color="black",
                                width=2.0,
                                alpha=0.8)
        plt.axis('off')
        plt.show()

    def basicInformation(country):
        frequencies = Counter(list(nx.get_node_attributes(country.cg, 'freq').values()))
        std = np.std(list(frequencies.values()))
        amt = len(list(frequencies.keys()))

        print("amount of frequencies: " + str(amt))
        print("standard deviation: " + str(std))
