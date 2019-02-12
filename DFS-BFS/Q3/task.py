from collections import defaultdict

class graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict(list)
        self.eSize = 0

    def addEdge(self,u,x):
        self.graph[u].append(x)
        self.graph[x].append(u)
        self.eSize += 1

def maxDistance(g):
    maxDis = 0
    for i in range(g.v):
        tmp = bfs(g,i)
        if(tmp > maxDis):
            maxDis = tmp
    return maxDis

def bfs(g,u):
        distance = [-1]*g.v
        distance[u] = 0
        q = []
        q.append(u)
        while(len(q) > 0):
            t = q.pop()
            for v in g.graph[t]:
                if(distance[v] == -1):
                    q.append(v)
                    distance[v] = distance[t] + 1

        return max(distance)
