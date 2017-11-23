class greedyHighDegreeSorted(algorithm):
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


class greedyLowDegreeSorted(algorithm):
    '''
    Returns the greedy algorithm based on the highest
    degree of the graph.
    '''
    def __init__(self, graph):
        degree = sorted([(n, graph.degree(n)) for n in graph.nodes()])
        #print(degree[0])
        for n in degree:
            graph.node[n[0]]['freq'] = 1
            while not algorithm.neighborCheck(graph, n[0]):
                graph.node[n[0]]['freq'] += 1


class greedyAlphabetically(algorithm):
    '''
    Returns the greedy algorithm based on
    an alphabeticaly sorted list
    '''
    def __init__(self, graph):
        for n in sorted(graph.nodes(), key=str.lower, reverse=False):
            graph.node[n]['freq'] = 1
            while algorithm.neighborCheck(graph, n) == False:
                graph.node[n]['freq'] += 1


class greedyReverseAlphabetically(algorithm):
    '''
    Returns the greedy algorithm based on
    an alphabeticaly sorted list
    '''
    def __init__(self, graph):
        for n in sorted(graph.nodes(), key=str.lower, reverse=True):
            graph.node[n]['freq'] = 1
            while algorithm.neighborCheck(graph, n) == False:
                graph.node[n]['freq'] += 1
