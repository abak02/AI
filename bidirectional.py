class Node:
    def __init__(self,val,neighbors=[]):
        self.val = val
        self.neighbors = neighbors
        self.parent_left = None
        self.parent_right = None
        self.visited_left = False
        self.visited_right = False

from collections import deque
def biredirection(s,t):
    def execute_node(node):
        node_copy=node
        path=[]
        while(node):
            path.append(node.val)
            node = node.parent_right

        path.reverse()
        del path[-1]
        
        while(node_copy):
            path.append(node_copy.val)
            node_copy = node_copy.parent_left
        return path

    q = deque([])
    q.append(s)
    q.append(t)
    s.visited_right=True
    t.visited_left=True

    while len(q)>0:
        n= q.pop()
        if n.visited_right and n.visited_left:
            return execute_node(n)
        
        for node in n.neighbors:
            if n.visited_left==True and not node.visited_left:
                node.parent_left = n
                node.visited_left = True
                q.append(node)
            if n.visited_right==True and not node.visited_right:
                node.parent_right = n
                node.visited_right = True
                q.append(node)
        
    return False



n0=Node(0)
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)

n0.neighbors = [n1, n5]
n1.neighbors = [n0, n2, n6]
n2.neighbors = [n1]
n3.neighbors = [n4, n6]
n4.neighbors = [n3]
n5.neighbors = [n0, n6]
n6.neighbors = [n1, n3, n5, n7]
n7.neighbors = [n6]

print(biredirection(n1,n4))