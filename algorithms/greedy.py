import networkx as nx
import matplotlib.pyplot as pyplot

from algorithms import algorithm

class greedy(algorithm):
    def __init__(self, graph, sortingType='alphabetical', reverse=False):
        '''
        Assigns frequencies to the graph with a greedy method. The input list
        can be sorted in different ways for different outputs.

        Args:
            graph (networkx graph)      : a networkx graph that is to be
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
        if sortingType == 'alphabetical':
            nodeList = sorted(graph.nodes(), key=str.lower, reverse=reverse)
        elif sortingType == 'degreeAscending':
            nodeList = sorted([(n, graph.degree(n)) for n in graph.nodes()],
                                key=lambda x: x[1], reverse=reverse)

        for n in graph.nodes():
            graph.node[n]['freq'] = 1
            while not algorithm.neighborCheck(graph, n):
                graph.node[n]['freq'] += 1

        print(algorithm.graphCheck(graph))
