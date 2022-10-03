## This is python program to implement graphs with the help of python dictionary
from collections import defaultdict
graph=defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
def generate_edges(graph):
    edges=[]
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node,neighbour))
    return edges
def find_path(graph,start,end,path=[]):
    path= path+[start]
    if start==end:
        return path
    for node in graph[start]:
        if node not in path:
            new_path=find_path(graph,node,end,path)
            if new_path:
                return new_path                       
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
  
# Driver Function call 
# to print generated graph
print(generate_edges(graph))      
print(find_path(graph, 'e', 'c'))           
