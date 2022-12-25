from collections import defaultdict
class Graph:
    def __init__(self,node):
        self.node = node
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            print(node,'->',self.graph[node])
    def DLS(self,src,target,maxdepth):
        if src == target:
            return True
        if maxdepth<=0:
            return False

        for i in self.graph[src]:
            if(self.DLS(i,target,maxdepth-1)):
                return True
        return False

    def IDDFS(self,src,target,maxdepth):
        for i in range(maxdepth):
            if(self.DLS(src,target,i)):
                return True
        return False

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)

g.print_graph()

src = 0
target =5
maxdepth=3

if(g.IDDFS(src,target,maxdepth)):
    print("Paoa geche")
else:
    print("paoa Jaini")