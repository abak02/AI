from collections import defaultdict
from queue import Queue
class Graph:
    def __init__(self,Nodes):
        self.nodes = Nodes
        self.adj_list = defaultdict(list)

    def add_edge(self,u,v):
        self.adj_list[u].append(v)

    def print_graph(self):
        for node in self.adj_list:
            print(node,'->',self.adj_list[node])

nodes = ["A", "B", "C", "D", "E", "F","G"]
graph = Graph(nodes)
all_edges =[("A","B"),("A","C"),("B","D"),("B","E"),("C","F"),("C","G")]
for u,v in all_edges:
    graph.add_edge(u,v)
graph.print_graph()

def bfs(start_node):
    visited = {}
    parent = {}
    bfs_out = []

    for v in graph.adj_list:
        visited[v] = False
        parent[v] = None

    visited[start_node] = True
    parent[start_node] = None

    q = Queue()
    q.put(start_node)
    while not q.empty():
        v = q.get()
        bfs_out.append(v)
        for u in graph.adj_list[v]:
            visited[u]=True
            parent[u] = v
            q.put(u)
    
    return bfs_out

print(bfs("A"))
