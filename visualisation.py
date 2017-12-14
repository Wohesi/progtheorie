import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import itertools
from collections import Counter


class visualisation:

    def distribution(countryList):

        # column = algorithm type
        # row = frequency
        # data = amount

        # the maximum frequency for the chart
        N = 7

        # initialise an empty pandas DataFrame with the right rows and columns
        columns = [c.algorithmType for c in countryList]
        index = list(range(1,8))
        data = {}

        for c in countryList:
            # construct a sorted tuple list of frequency amounts for each country
            attrDict = nx.get_node_attributes(c.cg, 'freq')
            freqCounts = [(k, len(list(g))) for
                            k,g in
                            itertools.groupby(sorted(attrDict.values()))]

            # continue with just the counts
            freqCounts2 = [x[1] for x in freqCounts]

            # pad the list with extra 0's for frequencies that don't exist
            if len(freqCounts2) < N:
                freqCounts2.extend([0] * (N - len(freqCounts2))) # extend the missing amount

            # add list to data dictionary for the right column
            data[c.algorithmType] = freqCounts2

        df = pd.DataFrame(data=data, index=index, columns=columns)

        ax = df.plot.bar(rot=0)
        plt.title(countryList[0].countryName)
        ax.set_ylabel("Frequency Amount")
        ax.set_xlabel("Frequency Type")
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

        # standard deviation
        std = np.std(list(frequencies.values()))

        # coefficient of variation
        cv = std / np.mean(list(frequencies.values()))

        # amount of frequencies
        amt = len(list(frequencies.keys()))

        print("country name: " + country.countryName)
        print("algorithm type: " + country.algorithmType)
        print("amount of frequencies: " + str(amt))
        print("standard deviation: " + str(std))
        print("coefficient of variation: " + str(cv))
        print("")
