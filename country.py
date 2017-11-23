import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from collections import Counter
from algorithms import greedy

class country:

    cg = nx.Graph()
    countryName = ""

    def __init__(self, name, csvfile):
        self.countryName = name

        with open(csvfile, encoding="utf8") as csvfile:
            countryFile = csv.reader(csvfile)
            provincePairs = [pair for pair in countryFile][1:]
            provinceNames = list(set(x[0] for x in provincePairs))

        # adding names and pairs to Graph
        self.cg = nx.Graph()
        self.cg.add_nodes_from(provinceNames, freq=None)
        self.cg.add_edges_from(provincePairs)




    def visualisation(self):
        # c = {1: 'red', 2: 'yellow', 3: 'green', 4: 'cyan',
        # 5: 'blue', 6: 'magenta', 7: 'orange'}
        # freqDict = nx.get_node_attributes(self.cg, 'freq')
        # colorDict = {node: c[node] for node in freqDict}
        # colors = list(zip(colorDict, colorDict.values()))

        nx.spring_layout(self.cg)

        plt.figure(figsize=(15,15))

        pos = nx.spring_layout(self.cg)
        nx.draw_networkx_nodes(self.cg, pos,
                                nodelist=self.cg.nodes(),
                                node_color='yellow', # change this
                                alpha=0.4)
        nx.draw_networkx_labels(self.cg, pos,
                                nodelist=self.cg.nodes(),
                                font_size=14)
        nx.draw_networkx_edges(self.cg, pos,
                                edgelist=self.cg.edges(),
                                edge_color="grey")
        plt.axis('off')
        plt.show()

    def distribution(self):
        freqfreq = Counter(list(nx.get_node_attributes(self.cg, 'freq').values()))

        radioFrequencies = freqfreq.keys()
        freqFrequencies = freqfreq.values()
        y_pos = np.arange(len(radioFrequencies))

        plt.bar(y_pos, freqFrequencies, align='center', alpha=0.5)
        plt.xticks(y_pos, radioFrequencies)
        plt.ylabel('Frequency')
        print(self.countryName, freqFrequencies)
        plt.title('Frequency of radio frequencies in ' + self.countryName)


        plt.show()
