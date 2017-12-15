import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import sys
import itertools
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

    def getLowestCost(self, costScheme, advanced=0):
        '''
        Calculates the lowest cost for the given cost scheme. It takes into
        account all possible permutations of this scheme.
        Args:
            costScheme (list) : a list of integers
        '''
        lowestCost = 999999999999999999999999
        optimalScheme = []
        permutations = list(itertools.permutations(costScheme))

        for c in permutations:
            if self.calcCost(c, advanced) < lowestCost:
                lowestCost = self.calcCost(c, advanced)
                optimalScheme = c


        print("country name: " + self.countryName)
        print("algorithm type: " + self.algorithmType)
        print("lowest cost: " + str(lowestCost))
        print("scheme used: " + str(optimalScheme))
        print("")

        return lowestCost

    def calcCost(self, costScheme, advanced):
        '''
        Calculates the cost of a single given cost scheme.
        Args:
            costScheme (list) : a list of integers
        '''


        cost = 0
        freqCounts = Counter(nx.get_node_attributes(self.cg, 'freq').values())

        if(advanced != 0):
            cost = self.advancedCostScheme(costScheme, freqCounts.keys(), advanced)

        for i,c in enumerate(costScheme):
            # the cost scheme has more frequencies than the country because
            # our algorithms work well, so we only count it is actually used
            if i+1 in list(freqCounts.keys()):
                # amount of times the frequency is used * the cost of it
                cost += freqCounts[i+1] * c
            else:
                return cost

        return cost

    def costRecursive(self,x,z,y):

        if z == 0:
            return 0
        else:
            return (x + self.costRecursive(x+y,z-1, y))

    def advancedCostScheme(self,x,z,y):
         # gives the the final price of the custom scheme
         #after the advanced calculations
         return sum([self.costRecursive(j[0],j[1], y) for j in list(zip(x,z))])
