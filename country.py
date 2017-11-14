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


<<<<<<< HEAD
UA  = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
USA  = country("United States of America", "csv-borders/USACompleteDataset.csv")
RU  = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
CN  = country("China", "csv-borders/ChinaCompleteDataset.csv")
=======
Ukraine  = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
>>>>>>> e0355c1a3f2c657446d493d993cce3b24abaa8e7
