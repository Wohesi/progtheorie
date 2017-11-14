import csv
import networkx as nx
import matplotlib.pyplot as plt

class country:

    def __init__(self, name, csvfile):
        #print(csvfile)
        with open(csvfile, encoding="utf8") as csvfile:
            countryFile = csv.reader(csvfile)
            provincePairs = [pair for pair in countryFile][1:]
            #print(provincePairs)
            provinceNames = list(set(x[0] for x in provincePairs))
            print (len(provinceNames))
            #print (provinceNames)

        cg = nx.Graph()
        cg.add_nodes_from(provinceNames)
        cg.add_edges_from(provincePairs)

        nx.spring_layout(cg)

        plt.figure(figsize=(15,15))

        pos = nx.spring_layout(cg)
        nx.draw_networkx_nodes(cg, pos,
                                nodelist=cg.nodes(),
                                node_color="yellow",
                                alpha=0.4)
        nx.draw_networkx_labels(cg, pos,
                                nodelist=cg.nodes(),
                                font_size=14)
        nx.draw_networkx_edges(cg, pos,
                                edgelist=cg.edges(),
                                edge_color="grey")
        plt.axis('off')
        plt.show()

UA  = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
USA  = country("United States of America", "csv-borders/USACompleteDataset.csv")
RU  = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
CN  = country("China", "csv-borders/ChinaCompleteDataset.csv")
