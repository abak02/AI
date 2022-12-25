from collections import defaultdict
class Graph:
    def __init__(self,Nodes):
        self.nodes = Nodes
        self.graph = defaultdict(list)

    def add_edge(self,u,v,weight):
        value = (v,weight)
        self.graph[u].append(value)

    def print_graph(self):
        for node in self.graph:
            print(node, '->',self.graph[node])

nodes = ['S',"B","C","D","E","F","G"]
gr=Graph(nodes)
all_edges=[('S','B',4),('S','C',3),('B','F',5),('B','E',12),('C','E',10),('C','D',7),('D','E',2),('F','G',16),('E','G',5)]
def heuristic(n):
    list={
        'S':14,
        'B':12,
        'C':11,
        'D':6,
        'E':4,
        'F':11,
        'G':0
    }
    return  list[n]
for u,v,w in all_edges:
    gr.add_edge(u,v,w)
gr.print_graph()

def astar(start,goal):
    open_set=set(start)
    close_set=set()
    g={}
    parent={}
    g[start]=0
    parent[start]=start
    while len(open_set)>0:
        n = None
        for v in open_set:
            if n == None or g[v]+heuristic(v)<g[n]+heuristic(n):
                n = v
        if n == goal or gr.graph[n] == None:
            pass
        else:
            for m,weight in gr.graph[n]:
                if m not in open_set and m not in close_set:
                    open_set.add(m)
                    parent[m]=n
                    g[m]=g[n]+weight
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parent[m]=n
                        if m in close_set:
                            close_set.remove(m)
                            open_set.add(m)
        if n==None:
            print("Path doesn't exist")
            return None
        if n == goal:
            path=[]
            while parent[n]!=n:
                path.append(n)
                n= parent[n]
            path.append(start)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        open_set.remove(n)
        close_set.add(n)
    
    print('Path does not exist!')
    return None
astar("S","G")
        