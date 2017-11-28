import networkx as nx
import matplotlib.pyplot as pyplot

from algorithms import algorithm

class backtracking(algorithm):
    def __init__(self, graph, currentN, listN, maxFreq):
        '''
        backtracking algoritme
        parameters:
        graph:          the graph you want to colour, and to get algorithm functions.
        currentN:       the current node that is being checked.
        listN:          list of nodes that are checked.
        maxFreq:        maximum amount of frequencies allowed in the graph.
        '''
        if graphCheck:
            return []

        currentN['freq'] = 1
        neighborCheck(currentN):
        if ! neighborCheck:

            if currentN['freq'] > maxFreq:
                backtracking(graph,
                            listN[i-1],
                            listN,
                            maxFreq)
            
            backtracking(graph,
                        listN[i+1],
                        listN,
                        maxFreq)
