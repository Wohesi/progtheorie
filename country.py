import csv
import networkx as nx
import itertools
from collections import Counter

class country:

    cg = nx.Graph()
    countryName = ""
    algorithmType = None

    def __init__(self, name, csvfile):
        '''
        Args:
            name (String)     : a country name
            csvfile (String)  : the location of the neighbor csv file
                                (located in the csv-borders folder)
        '''
        self.countryName = name

        with open(csvfile, encoding="utf8") as csvfile:
            countryFile = csv.reader(csvfile)
            provincePairs = [pair for pair in countryFile][1:]
            provinceNames = list(set(x[0] for x in provincePairs))

        # adding names and pairs to Graph
        self.cg = nx.Graph()
        self.cg.add_nodes_from(provinceNames, freq=None)
        self.cg.add_edges_from(provincePairs)

    def getLowestCost(self, costScheme):
        '''
        Calculates the lowest cost for the given cost scheme. It takes into
        account all possible permutations of this scheme.
        Args:
            costScheme (list) : a list of integers
        '''
        lowestCost = 999999999999999999999999
        optimalScheme = []

        # each permutation of the cost scheme has to be tried to make sure
        # we select the best assignment of costs to frequencies
        permutations = list(itertools.permutations(costScheme))

        for c in permutations:
            if self.calcCost(c) < lowestCost:
                lowestCost = self.calcCost(c)
                optimalScheme = c


        print("country name: " + self.countryName)
        print("algorithm type: " + self.algorithmType)
        print("lowest cost: " + str(lowestCost))
        print("scheme used: " + str(optimalScheme))
        print("")

        return lowestCost

    def calcCost(self, costScheme):
        '''
        Calculates the cost of a single given cost scheme.
        Args:
            costScheme (list) : a list of integers signifying the costs
        '''
        cost = 0
        freqCounts = Counter(nx.get_node_attributes(self.cg, 'freq').values())

        for i,c in enumerate(costScheme):
            # the cost scheme has more frequencies than the country because
            # our algorithms work well, so we only count it is actually used
            if i+1 in list(freqCounts.keys()):
                # amount of times the frequency is used * the cost of it
                cost += freqCounts[i+1] * c
            else:
                return cost

        return cost
