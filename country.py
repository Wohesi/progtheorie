import csv
import networkx as nx
import matplotlib.pyplot as plt

from algorithms import greedy

class country:

    cg = nx.Graph()

    def __init__(self, name, csvfile):
        #print(csvfile)
        with open(csvfile, encoding="utf8") as csvfile:
            countryFile = csv.reader(csvfile)
            provincePairs = [pair for pair in countryFile][1:]
            provinceNames = list(set(x[0] for x in provincePairs))

        # adding names and pairs to Graph
        self.cg = nx.Graph()
        self.cg.add_nodes_from(provinceNames, freq=None)
        self.cg.add_edges_from(provincePairs)




    def visualisation(self):
        # TODO Actually colour the graph
        nx.spring_layout(self.cg)


        plt.figure(figsize=(15,15))

        pos = nx.spring_layout(self.cg)
        nx.draw_networkx_nodes(self.cg, pos,
                                nodelist=self.cg.nodes(),
                                node_color="yellow",
                                alpha=0.4)
        nx.draw_networkx_labels(self.cg, pos,
                                nodelist=self.cg.nodes(),
                                font_size=14)
        nx.draw_networkx_edges(self.cg, pos,
                                edgelist=self.cg.edges(),
                                edge_color="grey")
        plt.axis('off')
        plt.show()

UA  = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
USA  = country("United States of America", "csv-borders/USACompleteDataset.csv")
RU  = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
CN  = country("China", "csv-borders/ChinaCompleteDataset.csv")

# UA.visualisation()
# USA.visualisation()
# RU.visualisation()
# CN.visualisation()

greedy(UA.cg)
# print(nx.get_node_attributes(UA.cg, 'freq'))

greedy(USA.cg)
# print(nx.get_node_attributes(USA.cg, 'freq'))
#
greedy(RU.cg)
# print(nx.get_node_attributes(RU.cg, 'freq'))
#
greedy(CN.cg)
# print(nx.get_node_attributes(CN.cg, 'freq'))
