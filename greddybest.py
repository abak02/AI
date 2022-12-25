from collections import defaultdict
from queue import PriorityQueue
class Graph:
    def __init__(self,Nodes):
        self.nodes = Nodes
        self.adj_list = defaultdict(list)

    def add_edge(self,u,v,w):
        value=(v,w)
        self.adj_list[u].append(value)
        value=(u,w)
        self.adj_list[v].append(value)

    def print_graph(self):
        for node in self.adj_list:
            print(node,'->',self.adj_list[node])

nodes = ["A", "B", "C", "D", "E", "F"]
graph = Graph(nodes)
all_edges =[("A","B",2),("A","C",1),("B","C",1),("B","E",2),("C","E",4),("D","F",2),("E","F",1)]
for u,v,w in all_edges:
    graph.add_edge(u,v,w)
graph.print_graph()

def greedy_best(start_node, end_node):
    visited ={}
    output=[]

    for node in graph.adj_list:
        visited[node] = False

    pq = PriorityQueue()
    pq.put((0,start_node))
    visited[start_node] = True

    while not pq.empty():
        item = pq.get()[1]
        output.append(item)

        if item == end_node:
            break
        for v,c in graph.adj_list[item]:
            if visited[v] == False:
                visited[v]=True
                pq.put((c,v))
    print(output)

greedy_best('A','F')

