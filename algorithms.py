import networkx as nx
import matplotlib.pyplot as pyplot

class algorithm:

    def pairCheck(graph, node1, node2):
        '''
        Returns True if both nodes don't share a radio frequency.
        '''
        # TODO Deal with None better.
        if graph.node[node1]['freq'] is not None and graph.node[node2]['freq'] is not None and graph.node[node1]['freq'] == graph.node[node2]['freq']:
            return False
        return True

    def neighborCheck(graph, node):
        '''
        Returns True if node doens't share a frequency with any of its neighbours.
        '''
        for neighbor in nx.all_neighbors(graph, node):
            if not algorithm.pairCheck(graph, node, neighbor):
                return False
        return True

    def graphCheck(graph):
        '''
        Returns True if all nodes don't share a frequency with any of their neighbours.
        '''
        for node in graph.nodes():
            if not algorithm.neighborCheck(graph, node):
                return False

        if None in nx.get_node_attributes(graph, 'freq').values():
            return False

        return True

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

class DSatur(algorithm):
    def __init__(self, graph):
        '''
        take node with highest degree
        colour it
           v
        1 take node with highest saturation (most coloured neighbours)
        2 colour it
        3 repeat (recursion)
        '''
        attrDict = nx.get_node_attributes(graph, 'freq')
        attrList = [[   k,
                        attrDict[k],
                        self.getSaturation(graph, k),
                        graph.degree(k)] for k in attrDict]
        sortedList = sorted(attrList, key = lambda x: (x[2], x[3]), reverse=True)
        # sort by saturation, then by degree in descending order
        result = self.recursiveColor(graph, sortedList, [])

        print(result)

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
        # testing
        print("done: " + str(len(doneList)))
        print("node: " + str(len(nodeList)))
        print("")
        if len(nodeList) != 0:
            print(nodeList[0][0])

        # Return if no nodes are left to colour in
        if nodeList == []:
            return []

        # Loop to set colour so it doesn't interfere with neighbours
        nodeList[0][1] = 1
        # NEIGHBORCHECK DOES NOT WORK
        # GRAPH DOESN'T GET UPDATED IN RECURSION
        # EITHER UPDATE GRAPH IN THIS FUNCTION DYNAMICALLY
        # OR REWRITE NEIGHBORCHECK FUNCTION (MORE DIFFICULT)
        print(algorithm.neighborCheck(graph, nodeList[0][0]))
        while not algorithm.neighborCheck(graph, nodeList[0][0]):
            nodeList[0][1] += 1
            print(algorithm.neighborCheck(graph, nodeList[0][0]))

        # update graph with new Frequency
        # (important for checking neighbours during recursion)
        graph.node[nodeList[0][0]]['freq'] = nodeList[0][1]

        # add the newly coloured in node to the donelist
        newDoneList = doneList + [nodeList[0]]
        
        # New nodelist without the node that was just coloured in
        # with newly calculated saturations
        newNodeList = [[    n[0],
                            n[1],
                            self.getSaturation(graph, n[0]),
                            n[3]]  for n in nodeList[1:]]

        return self.recursiveColor(graph, newNodeList, newDoneList)
