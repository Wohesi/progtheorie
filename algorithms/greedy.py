import networkx as nx
import matplotlib.pyplot as pyplot

from algorithms import algorithm

class greedy(algorithm):
    def __init__(self, country, sortingType='alphabetical', reverse=False):
        '''
        Assigns frequencies to the graph with a greedy method. The input list
        can be sorted in different ways for different outputs.

        Args:
            country (country object)    : a country object that is to be
                                          processed. Note: the nodes should have
                                          an attribute 'freq' set to None.
            sortingType (string): the type of sorting the method uses.
                Choose from:
                'alphabetical' (default):   alphabetically
                'degree'                :   based on the degree of each node
            reverse (boolean): whether the sorting is reversed or not.
                'True'                  :   the list is reversed
                'False'        (default):   the list is not reversed
        '''

        nodeList = []
        graph = country.cg
        if sortingType == 'alphabetical':
            nodeList = sorted(graph.nodes(), key=str.lower, reverse=reverse)
        elif sortingType == 'degree':
            nodeList = sorted([n for n in graph.nodes()],
                                key=lambda x:  (graph.degree(x), x), reverse=reverse)

        for n in nodeList:
            graph.node[n]['freq'] = 1
            while not algorithm.neighborCheck(graph, n):
                graph.node[n]['freq'] += 1

        country.algorithmType = "Greedy " + sortingType
        print(country.countryName + " was sorted using the greedy algorithm!")
        print("graphCheck returns " + str(algorithm.graphCheck(graph)))
