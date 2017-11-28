import networkx as nx
import matplotlib.pyplot as pyplot

from algorithms import algorithm

class backtracking(algorithm):
    def __init__(self, graph, maxFreq):
        '''
        backtracking algoritme
        parameters:
        graph:          the graph you want to colour, and to get algorithm functions.
        currentN:       the current node that is being checked.
        listN:          list of nodes that are checked.
        maxFreq:        maximum amount of frequencies allowed in the graph.
        '''
        attrDict = nx.get_node_attributes(graph, 'freq')
        listN = [   n,
                    attrDict[n],
                    i for n, i in enumerate(attrDict.keys())]


    def backTrackColouring(self, graph, currentN, listN, maxFreq)
        if graphCheck:
            return []

        if currentN['Freq'] == None:
            currentN = 1
        else:
            currentN += 1

        neighborCheck(currentN):

        if ! neighborCheck:

            currentN['freq'] + 1 if currentN['freq'] + 1 is not > maxFreq

            if currentN['freq'] > maxFreq:
                backtracking(graph,
                            listN[i-1],
                            listN,
                            maxFreq)

            return [currentN] + backtracking(graph,
                                            listN[i+1],
                                            listN,
                                            maxFreq)
