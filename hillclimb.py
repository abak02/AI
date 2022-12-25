graph = {'A': {'B', 'C'},
         'B':{'A', 'D', 'E'},
         'C': {'A', 'F','G'},
         'D': {'B','H','I'},
         'E': {'B'},
         'F': {'C', 'J'},
         'G':{'C','L'},
         'H':{'D'},
         'I':{'D'},
         'J':{'F'},
         'L':{'G'}
}
node_data={
    'A':{'h':5},
    'B':{'h':3},
    'C':{'h':2},
    'D':{'h':2},
    'E':{'h':3},
    'F':{'h':2},
    'G':{'h':3},
    'H':{'h':1},
    'I':{'h':99},
    'J':{'h':99},
    'L':{'h':0}
}

def HillClimbing(graph,start,goal):
    visited=[]
    temp=start
    
    while temp!=goal:
        if temp not in visited:
            visited.append(temp)
        (h,p)=(node_data[temp]['h'],temp)
        flag=True
        for j in graph[temp]:
            if j not in visited:
                if node_data[j]['h']<=h:
                    h=node_data[j]['h']
                    p=j
                    flag=False
        if flag:
            print("loacl maxima solution:")
            return list(temp)
        else:
            temp=p
    print("Global Maxima solution:")      
    return list(goal)          

HillClimbing(graph,'A','F')
          


