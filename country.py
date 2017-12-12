import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.insert(0,'algorithms')

from collections import Counter
#from algorithms import greedy
import greedy

class country:

    cg = nx.Graph()
    countryName = ""
    algorithmType = None

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
