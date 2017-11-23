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

# class dSatur(algorithm):
#     '''
#
#     '''
#     def __init__(self, graph):
