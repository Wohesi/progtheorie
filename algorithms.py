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
    def __init__(self, graph):
        '''
        Returns the basic greedy algorithm.
        '''
        for n in graph.nodes():
            graph.node[n]['freq'] = 1
            while not algorithm.neighborCheck(graph, n):
                graph.node[n]['freq'] += 1



class greedyDegreeSorted(algorithm):
    '''
    Returns the greedy algorithm based on the highest
    degree of the graph.
    '''
    def __init__(self, graph):
        degree = sorted([(n, graph.degree(n)) for n in graph.nodes()], key=lambda x: x[1], reverse = True)
        #print(degree[0])
        for n in degree:
            graph.node[n[0]]['freq'] = 1
            while not algorithm.neighborCheck(graph, n[0]):
                graph.node[n[0]]['freq'] += 1


class dSatur(algorithm):
    '''
    '''
    def __init__(self, graph):
