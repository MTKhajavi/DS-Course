from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

def countPaths(g, s, d):
    visited =[False for _ in range(g.V)]
    count = []
    dfs(g, s, d,visited, count)
    return len(count)

def dfs(g, s, d,visited, count):
    visited[s]= True
    if s == d:
        count += [1]
    else:
        for i in g.graph[s]:
            if not visited[i]:
                dfs(g, i, d, visited, count)

    visited[s] = False
