import networkx as nx
import matplotlib.pyplot as pyplot
import copy

from algorithms import algorithm
from dsatur import DSatur

import sys
sys.path.insert(0,'algorithms')
sys.path.insert(0,'bin')

class backtracking(algorithm):

    def __init__(self, country, maxFreq):
        '''
        parameters:
        country:        The country you want to have a frequncy distribution of
        maxFreq:        the maximum amount of frequencies used
        '''
        if(True):
            DSatur(country)
        else:
            graph = country.cg
            attrDict = nx.get_node_attributes(graph, 'freq')
            nodeList = [ [x,                                         # name
                         attrDict[x] ]                              # freq
                         for x in attrDict.keys()]

            print(self.backTrackColouring(graph, nodeList, 0, maxFreq))


    def backTrackColouring(self, graph, nodeList, n, maxFreq):
        '''
        backtracking algoritme
        parameters:
        graph:          the graph you want to colour, and to get algorithm functions.
        currentN:       the current node that is being checked.
        nodeList:       list of nodes that are checked.
        maxFreq:        maximum amount of frequencies allowed in the graph.
        '''
        # If there are no interferences in the graph, return an empty list
        if n > len(nodeList):
            return nodeList
        if algorithm.graphCheck(graph):
            return nodeList

        # Adds a frequency to the first node
        if nodeList[0][1] == None:
            nodeList[0][1] = 1
            graph.node[nodeList[0][0]]['freq'] = 1
        # if it already has a frequncy (backtracking) sets it to the next one
        else:
            nodeList[0][1] += 1
            graph.node[nodeList[0][0]]['freq'] += 1

        while not algorithm.neighborCheck(graph,nodeList[0][0]):
            nodeList[0][1] += 1
            graph.node[nodeList[0][0]]['freq'] += 1

            if graph.node[nodeList[0][0]]['freq'] >= maxFreq:
                nodeList[0][1] = None
                graph.node[nodeList[0][0]]['freq'] = None

                newNodeList = [nodeList[-1]] + nodeList[:-1]
                # return [nodeList[0]] + self.backTrackColouring(graph,
                #             newNodeList,
                #             maxFreq)
                nn = n + 1
                return self.backTrackColouring(graph,
                            newNodeList,
                            nn,
                            maxFreq)


        newNodeList = nodeList[1:] + [nodeList[0]]
        # return [nodeList[0]] + self.backTrackColouring(graph,
        #         newNodeList,
        #         maxFreq)

        nn = n + 1
        return self.backTrackColouring(graph,
                    newNodeList,
                    nn,
                    maxFreq)

# Geef een node een frequentie
# Als twee nodes dezelfde frequentie hebben
    # geef de huidige node een hogere frequentie
    # Als deze nieuwe frequntie hoger is dan het maximaal toegestane frequrntie
    # verander de frequentie van de vorige node
    # Probeer opnieuw een frequentie toe te wijzen
    # r e p e a t
