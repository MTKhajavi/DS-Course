
def intersect(l1, r1, l2, r2):
    if l1 <= l2 and r1 >= r2 or l2 <= l1 and r2 >= r1:
        return False
    if r2 <= r1 and l1 <= l2 and r2 <= l2:
        return False
    if l1 >= r2 and l1 >= l2 or r1 <= l2 and r1 <= r2:
        return False
    return True

def ans(color):
    return ''.join(['I' if i == 0 else 'O' for i in color])


def dfs(v, clr, color, graph):
    if color[v] != -1 and color[v] != clr:
        return 'Impossible'
    if color[v] != -1:
        return
    color[v] = clr
    for u in graph[v]:
        if dfs(u, 1 - clr, color, graph) == 'Impossible':
            return 'Impossible'

# Sample Input:
# Input = [[4, 2], [1, 3], [2, 4]]

def solve(input):
    n, m = input[0]
    graph = [[] for i in range(m)]
    vedge = []
    color = [-1] * m
    for i in range(m):
        a, b = map(int, input[i + 1])
        a, b = min(a, b), max(a, b)
        for j, v in enumerate(vedge):
            if intersect(a, b, v[0], v[1]):
                graph[i].append(j)
                graph[j].append(i)
        vedge.append((a, b))

    for i in range(m):
        if color[i] == -1:
            if dfs(i, 0, color, graph):
                return 'Impossible'
    return ans(color)
