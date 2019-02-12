import copy


class Graph:
    def __init__(self, N):
        self.graph = [[] for _ in range(N)]
        self.Vertices_num = N
        self.result = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def all_topologicals(self):
        visited = [False for _ in range(self.Vertices_num)]
        in_degree = [0 for _ in range(self.Vertices_num)]
        for i in range(self.Vertices_num):
            for j in self.graph[i]:
                in_degree[j] += 1

        answers = []
        self.find_topological(visited, in_degree, answers)
        return self.result

    def find_topological(self, visited, in_degree, answers):
        flag = False
        for i in range(self.Vertices_num):
            if in_degree[i] == 0 and not visited[i]:
                visited[i] = True
                answers.append(i)
                for j in self.graph[i]:
                    in_degree[j] -= 1
                self.find_topological(visited, in_degree, answers)

                visited[i] = False
                del answers[-1]
                for j in self.graph[i]:
                    in_degree[j] += 1
                flag = True
        if not flag:
            a = copy.deepcopy(answers)
            self.result.append(a)


# Don't change this function
def solve(graph):
    return graph.all_topologicals()


