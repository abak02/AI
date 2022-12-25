from collections import defaultdict
from queue import PriorityQueue

class Graph:
    def __init__(self,Nodes):
        self.nodes = Nodes
        self.adj_list = defaultdict(list)

    def add_edge(self,u,v,w):
        value=(v,w)
        self.adj_list[u].append(value)

    def print_graph(self):
        for node in self.adj_list:
            print(node,'->',self.adj_list[node])

    def ucs(self,current_node,goal_node):
        visited = []
        pq = PriorityQueue()
        pq.put((0,current_node))


        while not pq.empty():
            current_node =pq.get()[1]

            if current_node == goal_node:
                print(current_node, end = ' ')
                pq.queue.clear()
            else:
                if current_node in visited:
                    continue
            
                print(current_node, end = ' ')
                visited.append(current_node)

                for node in self.adj_list[current_node]:
                    pq.put((node[1],node[0]))


nodes = ["S","A","B","C","D","G"]
g = Graph(nodes)
g.add_edge('S', 'A', 1)
g.add_edge('S', 'G', 12)
g.add_edge('A', 'B', 3)
g.add_edge('A', 'C', 1)
g.add_edge('C', 'D', 1)
g.add_edge('B', 'D', 3)
g.add_edge('C', 'G', 2)
g.add_edge('D', 'G', 3)
g.print_graph()
g.ucs('S','G')