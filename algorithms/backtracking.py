import networkx as nx
import matplotlib.pyplot as pyplot

from algorithms import algorithm

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
        graph = country.cg
        attrDict = nx.get_node_attributes(graph, 'freq')
        nodeList = [ [i,                                        # id
                     x,                                         # name
                     attrDict[x] ]                              # freq
                     for i,x in enumerate(attrDict.keys())]

        self.backTrackColouring(graph, nodeList[0], nodeList, maxFreq)


    def backTrackColouring(self, graph, currentN, nodeList, maxFreq):
        '''
        backtracking algoritme
        parameters:
        graph:          the graph you want to colour, and to get algorithm functions.
        currentN:       the current node that is being checked.
        nodeList:          list of nodes that are checked.
        maxFreq:        maximum amount of frequencies allowed in the graph.
        '''
        # If there are no interferences in the graph, return an empty list
        if algorithm.graphCheck:
            return []

        # Adds a frequency to node.
        if nodeList[0][2] == None:
            nodeList[0][2] = 1
        #print(self, graph, currentN, nodeList, maxFreq)

        # If neighbours interfere:
        if not algorithm.neighborCheck(graph, nodeList[0][1]):
            # Set the frequency + 1, if it's not the maximum Frequency
            #nodeList[0]['Freq'] + 1 if nodeList[0]['freq'] is not maxFreq
            if nodeList[0][2] <= maxFreq:
                nodeList[0][2] += 1

            # If the current frequency is highter than the maximum freq
            if nodeList[0][2] > maxFreq:
                backtracking(graph,
                            nodeList[1:],
                            nodeList,
                            maxFreq)

            return [nodeList[0]] + backTrackColouring(graph,
                                            currentN -1,
                                            nodeList,
                                            maxFreq)
