#import dictionary for graph
from collections import defaultdict
#function add edge to graph
graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
#definition of function    
def generate_edges(graph):
    edges = []
    for node in graph: #for nodes in graph
        for neighbor in graph [node]: #for neighbor
            edges.append((node,neighbor))
    return edges
#declare the graph as a dictionary 
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')

print(generate_edges(graph))#print graph to show pathways 