class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    def isSafe(self, i, j, visited):
        return (0 <= i < self.ROW and 0 <= j < self.COL and
                not visited[i][j] and self.graph[i][j])

    def dfs(self, i, j, visited):
        # These arrays are used to get row and
        # column numbers of 8 neighbours
        # of a given cell
        row_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[i][j] = True
        for k in range(8):
            if self.isSafe(i + row_nbr[k], j + col_nbr[k], visited):
                self.dfs(i + row_nbr[k], j + col_nbr[k], visited)

    def count_islands(self):
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] == False and self.graph[i][j] == 1:
                    self.dfs(i, j, visited)
                    count += 1
        return count


# Don't change this function
def solve(graph):
    return graph.count_islands()
