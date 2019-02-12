from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self,v,w):
        self.graph[v].append(w)
        self.graph[w].append(v)


def dfs(g,v,visited,parent):
    visited[v] = True
    for i in g.graph[v]:
        if not visited[i]:
            if dfs(g,i, visited, v):
                return True
        elif parent is not i:
            return True

    return False


def hasCycle(g):
    visited =[False for i in range(g.V)]
    for i in range(g.V):
        if not visited[i]:
            if dfs(g, i, visited, -1):
                return True

    return False
