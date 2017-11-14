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

#UA  = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
USA  = country("United States of America", "csv-borders/USACompleteDataset.csv")
#RU  = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
#CN  = country("China", "csv-borders/ChinaCompleteDataset.csv")
