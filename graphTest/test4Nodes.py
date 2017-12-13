import networkx as nx
import matplotlib.pyplot as plt


colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black']
letters = ['A', 'B', 'C', 'D']

neighbors = {}
neighbors['A'] = ['B', 'C']
neighbors['B'] = ['A', 'D', 'C']
neighbors['C'] = ['A', 'B', 'C']
neighbors['D'] = ['B', 'C']


#print (neighbors)
#print (neighbors.items())




c = {1: 'red', 2: 'yellow', 3: 'green', 4: 'cyan'}
def colour():
    nodesStates=list(neighbors.keys())
    edges = neighbors.items()
    #print(nodesStates)
    G=nx.Graph()
    G.add_nodes_from(nodesStates)
    test = c.items()
    print (test)
    #G.add_edges_from([('A' , 'B'),('C' , 'D')])
    #nx.draw(G, node_color=test)
    #plt.show(G)

colour()
