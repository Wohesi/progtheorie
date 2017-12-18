import csv
import networkx as nx
import itertools
from collections import Counter

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

    def getLowestCost(self, costScheme, advanced=0, advancedType="Percentage"):
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
            if self.calcCost(c, advanced, advancedType) < lowestCost:
                lowestCost = self.calcCost(c, advanced, advancedType)
                optimalScheme = c


        print("country name: " + self.countryName)
        print("algorithm type: " + self.algorithmType)
        print("lowest cost: " + str(lowestCost))
        print("scheme used: " + str(optimalScheme))
        print("")

        return lowestCost

    def calcCost(self, costScheme, advanced, advancedType):
        '''
        Calculates the cost of a single given cost scheme.
        Args:
            costScheme (list) : a list of integers
        '''


        cost = 0
        freqCounts = Counter(nx.get_node_attributes(self.cg, 'freq').values())

        if(advanced != 0):
            print(freqCounts.values())
            cost = self.advancedCostScheme(costScheme, freqCounts.values(), advanced, advancedType)

        for i,c in enumerate(costScheme):
            # the cost scheme has more frequencies than the country because
            # our algorithms work well, so we only count it is actually used
            if i+1 in list(freqCounts.keys()):
                # amount of times the frequency is used * the cost of it
                cost += freqCounts[i+1] * c
            else:
                return cost

        return cost

    def costRecursivePercentage(self,cost,freq,decreaseAmount):
        '''
        Calculates the cost recursively for frequencies
        '''
        if freq == 0:
            return 0
        else:
            return (cost + self.costRecursivePercentage(cost*decreaseAmount,freq-1, decreaseAmount))

    def costRecursiveFixedAmount(self,cost,freq,decreaseAmount):
        '''
        Calculates the cost recursively for frequencies
        '''
        if freq == 0:
            return 0
        else:
            return (cost + self.costRecursiveFixedAmount(cost-decreaseAmount,freq-1, decreaseAmount))

    def advancedCostScheme(self,costScheme,freqCounts,decreaseAmount, advancedType):
        '''
        Calculates the cost for a country given a single cost scheme according
        to the rules of the advanced assignment.
        '''
        if advancedType=="Percentage":
            return sum([self.costRecursivePercentage(j[0],j[1], decreaseAmount) for j in list(zip(costScheme,freqCounts))])
        if advancedType=="Fixed":
            return sum([self.costRecursiveFixedAmount(j[0],j[1], decreaseAmount) for j in list(zip(costScheme,freqCounts))])
