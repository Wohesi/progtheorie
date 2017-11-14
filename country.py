import csv
import networkx as nx
import matplotlib.pyplot as plt

class country:

    def __init__(self, name, csvfile):
        #print(csvfile)
        with open(csvfile) as csvfile:
            countryFile = csv.reader(csvfile)
            provincePairs = [pair for pair in countryFile]
            print(provincePairs)
            #countryWithBorders = [pair for pair in countryFile][1:]
            #provinceNames = lit(set(x[0] for x in countryWithBorders))


        #cg = nx.graph()
        #cg.add_nodes_from(csvfile)


USA  = country("USA", "csv-borders/UkraineCompleteDataset.csv")
