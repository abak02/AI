from collections import defaultdict
from queue import Queue
class Graph:
    def __init__(self,Nodes):
        self.nodes = Nodes
        self.adj_list = defaultdict(list)

    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_graph(self):
        for node in self.adj_list:
            print(node,'->',self.adj_list[node])

nodes = ["A", "B", "C", "D", "E", "F"]
graph = Graph(nodes)
all_edges =[("A","B"),("A","C"),("B","D"),("B","E"),("C","F"),("C","G")]
for u,v in all_edges:
    graph.add_edge(u,v)
#graph.print_graph()



color ={}
parent = {}
dfs_output = []

for v in graph.adj_list:
    color[v] ='W'
    parent[v] = None

def dfs_util(u):
    color[u]='G'
    dfs_output.append(u)
    for v in graph.adj_list[u]:
        if color[v] == 'W':
            parent[v]=u
            dfs_util(v)
    color[u]='B'


dfs_util('A')
print(dfs_output)