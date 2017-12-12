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
        # if algorithm.graphCheck:
        #     return []

        # Adds a frequency to node.

        for c in nodeList:

            if c[2] == None:
                graph.node[c[1]]['freq'] = 1

            while not algorithm.neighborCheck(graph,c[1]):
                graph.node[c[1]]['freq'] += 1

                if graph.node[c[1]]['freq'] <= maxFreq:
                    print ("too high")
                    return [graph, c[1:], nodeList, maxFreq]
                print(graph.node[c[1]]['freq'])

                # If the current frequency is highter than the maximum freq
                # if c[2] > maxFreq:
                #     backtracking(graph,
                #                 nodeList[1:],
                #                 nodeList,
                #                 maxFreq)

                # return [nodeList[0]] + backTrackColouring(graph,
                #                                 currentN -1,
                #                                 nodeList,
                #                                 maxFreq)
