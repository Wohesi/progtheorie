import networkx as nx
import copy

from algorithms import algorithm

import sys
sys.path.insert(0,'algorithms')
sys.path.insert(0,'bin')
sys.setrecursionlimit(10000)

class bktrk(algorithm):
    # MIGHT NOT WORK DUE TO PYTHON RECURSION LIMITS

    def __init__(self, country, maxFreq):
        graph = country.cg
        attrDict = nx.get_node_attributes(graph, 'freq')
        attrList = [[x, attrDict[x]] for x in attrDict.keys()]

        print(self.colorFirst(graph, attrList, maxFreq))

        country.algorithmType = "Backtracking"
        print(country.countryName + " was sorting using the backtracking algorithm!")
        print("graphCheck returns " + str(algorithm.graphCheck(graph)))


    def colorFirst(self, graph, nodeList, maxFreq):
        # WILL COLOUR IN THE FIRST NODE OF THE ATTRLIST

        # WE CAN STOP IF THE GRAPH IS ALREADY COLOURED IN CORRECTLY
        if algorithm.graphCheck(graph):
            return nodeList

        newList = copy.deepcopy(nodeList)

        # COLOUR IN THE FIRST NODE
        newList[0][1] = 1
        graph.node[newList[0][0]]['freq'] = 1

        # THE COLOURING CANT INTERFERE WITH IT'S NEIGHBOURS;
        # LOOP UNTIL IT'S LEGAL
        while not algorithm.neighborCheck(graph, newList[0][0]):
            newList[0][1] += 1
            graph.node[newList[0][0]]['freq'] += 1

        # IF THE VALID COLOURING EXCEEDS THE MAXIMUM, WE GOTTA BACKTRACK
        # PUT THE LAST NODE IN FRONT
        if newList[0][1] > maxFreq:
            newList[0][1] = None
            graph.node[newList[0][0]]['freq'] = None

            newerList = [newList[-1]] + newList[:-1]
            return self.colorFirst(graph, newerList, maxFreq)

        # IF IT DOESN'T EXCEED THE MAXIMUM, WE CAN PROCEED WITH THE NEXT NODE
        else:
            newerList = newList[1:] + [newList[0]]
            return self.colorFirst(graph, newerList, maxFreq)
