import networkx as nx
import matplotlib.pyplot as pyplot
import copy
import time

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
        graph = country.cg
        attrDict = nx.get_node_attributes(graph, 'freq')
        attrList = [[x, attrDict[x]] for x in attrDict.keys()]

        self.backTrackColouring(graph, attrList, maxFreq)

        country.algorithmType = "Backtracking"
        print(country.countryName + " was sorted using the backtracking algorithm!")
        print("graphCheck returns " + str(algorithm.graphCheck(graph)))


    def backTrackColouring(self, graph, nodeList, maxFreq):
        '''
        backtracking algoritme
        parameters:
        graph:          the graph you want to colour, and to get algorithm functions.
        currentN:       the current node that is being checked.
        nodeList:       list of nodes that are checked.
        maxFreq:        maximum amount of frequencies allowed in the graph. >=4
        '''
        if algorithm.graphCheck(graph):
            return True

        newList = copy.deepcopy(nodeList)

        while True:

            ## UNCOMMENT THIS TO  WATCH THE MAGIC HAPPEN IN REAL TIME
            ## SIT BACK AND ENJOY
            # attrDict = nx.get_node_attributes(graph, 'freq')
            # freqCounts = [k for
            #                 k in
            #                 attrDict.values()]
            # print(freqCounts)
            # print("")
            # print("")
            # time.sleep(0.1)


            if newList[0][1] == None:
                newList[0][1] = 1
                graph.node[newList[0][0]]['freq'] = 1
            else:
                newList[0][1] += 1
                graph.node[newList[0][0]]['freq'] += 1

            if newList[0][1] <= maxFreq:
                if algorithm.neighborCheck(graph, newList[0][0]):
                    if self.backTrackColouring(graph, newList[1:], maxFreq):
                        return True
            else:
                newList[0][1] = None
                graph.node[newList[0][0]]['freq'] = None
                return False
