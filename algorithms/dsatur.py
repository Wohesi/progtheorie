import networkx as nx
import matplotlib.pyplot as pyplot

from algorithms import algorithm

class DSatur(algorithm):
    def __init__(self, country):
        '''
        take node with highest degree
        colour it
           v
        1 take node with highest saturation (most coloured neighbours)
        2 colour it
        3 repeat (recursion)
        '''
        graph = country.cg
        attrDict = nx.get_node_attributes(graph, 'freq')
        attrList = [[   k,
                        attrDict[k],
                        self.getSaturation(graph, k),
                        graph.degree(k)] for k in attrDict]
        sortedList = sorted(attrList, key = lambda x: (x[2], x[3], x[0]), reverse=True)
        # sort by saturation, then by degree in descending order
        result = self.recursiveColor(graph, sortedList, [])

        country.algorithmType = "DSatur"
        print(country.countryName + " was sorting using the DSatur algorithm!")
        print("graphCheck returns " + str(algorithm.graphCheck(graph)))

    def getSaturation(self, graph, node):
        '''
        Returns the saturation (amount of coloured nodes) as an int.
        '''
        saturation = 0
        for neighbor in nx.all_neighbors(graph, node):
            if graph.node[neighbor]['freq'] != None:
                saturation += 1
        return saturation

    def recursiveColor(self, graph, nodeList, doneList):
        '''
        Takes a graph and a  list of structure [[node, freq, saturation, degree]]
        and assigns the frequencies.
        '''
        # Return if no nodes are left to colour in
        if nodeList == []:
            return []

        # Loop to set colour so it doesn't interfere with neighbours
        nodeList[0][1] = 1
        graph.node[nodeList[0][0]]['freq'] = 1

        # Update the frequency until it doesn't interfere with neighbours
        while not algorithm.neighborCheck(graph, nodeList[0][0]):
            nodeList[0][1] += 1
            graph.node[nodeList[0][0]]['freq'] += 1

        # add the newly coloured in node to the donelist
        newDoneList = doneList + [nodeList[0]]

        # New nodelist without the node that was just coloured in
        # with newly calculated saturations
        newNodeList = [[    n[0],
                            n[1],
                            self.getSaturation(graph, n[0]),
                            n[3]]  for n in nodeList[1:]]
        newNodeListSorted = sorted(newNodeList, key = lambda x: (x[2], x[3], x[0]), reverse=True)

        return newDoneList + self.recursiveColor(graph, newNodeListSorted, newDoneList)
