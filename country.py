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
        print(self.countryName)
        print(freqFrequencies)
        plt.title('Frequency of radio frequencies in ' + self.countryName)


        plt.show()
UA1  = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
USA1  = country("United States of America", "csv-borders/USACompleteDataset.csv")
RU1  = country("Russia", "csv-borders/NewRussiaCompleteDataset.csv")
CN1  = country("China", "csv-borders/ChinaCompleteDataset.csv")

greedy(UA1.cg, "degree")
greedy(USA1.cg, "degree")
greedy(RU1.cg, "degree")
greedy(CN1.cg, "degree")

UA2  = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
USA2  = country("United States of America", "csv-borders/USACompleteDataset.csv")
RU2  = country("Russia", "csv-borders/NewRussiaCompleteDataset.csv")
CN2  = country("China", "csv-borders/ChinaCompleteDataset.csv")

greedy(UA2.cg, "degree", True)
greedy(USA2.cg, "degree", True)
greedy(RU2.cg, "degree", True)
greedy(CN2.cg, "degree", True)

UA3  = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
USA3  = country("United States of America", "csv-borders/USACompleteDataset.csv")
RU3  = country("Russia", "csv-borders/NewRussiaCompleteDataset.csv")
CN3  = country("China", "csv-borders/ChinaCompleteDataset.csv")

greedy(UA3.cg, "alphabetical")
greedy(USA3.cg, "alphabetical")
greedy(RU3.cg, "alphabetical")
greedy(CN3.cg, "alphabetical")

UA4  = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
USA4  = country("United States of America", "csv-borders/USACompleteDataset.csv")
RU4  = country("Russia", "csv-borders/NewRussiaCompleteDataset.csv")
CN4  = country("China", "csv-borders/ChinaCompleteDataset.csv")

greedy(UA4.cg, "alphabetical", True)
greedy(USA4.cg, "alphabetical", True)
greedy(RU4.cg, "alphabetical", True)
greedy(CN4.cg, "alphabetical", True)


# UA.visualisation()
# USA.visualisation()
# RU.visualisation()
# CN.visualisation()

UA1.distribution()
USA1.distribution()
RU1.distribution()
CN1.distribution()

UA2.distribution()
USA2.distribution()
RU2.distribution()
CN2.distribution()

UA3.distribution()
USA3.distribution()
RU3.distribution()
CN3.distribution()

UA4.distribution()
USA4.distribution()
RU4.distribution()
CN4.distribution()
