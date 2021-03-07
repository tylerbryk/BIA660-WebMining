import networkx as nx

myGraph = nx.Graph()
file = open('input.txt')
for line in file:
    line = line.strip()
    toks = line.split(' ')
    myGraph.add_edge(toks[0],toks[1]) 
file.close()

print ('\nWE HAVE A GRAPH WITH ', myGraph.number_of_nodes(),'NODES AND ', myGraph.number_of_edges(),' EDGES.')
print ('THE GRAPH DIAMETER IS ', nx.diameter(myGraph))                                  
print ('NEIGHBORS OF NODE 32', myGraph.neighbors('32'))

myGraph.node['32']['name'] = 'Ted'
myGraph.node['32']['city'] = 'Hoboken'

myGraph['32']['25']['type'] = 'friends'
myGraph['32']['26']['type'] = 'colleagues'
myGraph['32']['26']['timestamp'] = 2011
print ('INFO FOR NODE 32', myGraph['32'])