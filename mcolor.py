def graphColoring(graph, m, n):
    color = [-1] * n

    def isSafe(node, col):
        for adj in range(n):
            if graph[node][adj] == 1 and color[adj] == col:
                return False
        return True

    def mcolor(node):
        if node == n:
            return True

        for col in range(m):
            if isSafe(node, col):
                color[node] = col
                if mcolor(node + 1):
                    return True
                color[node] = -1   # backtrack

        return False

    if mcolor(0):
        print("Coloring possible:", color)
        return True
    else:
        print("Coloring not possible")
        return False
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 3   # number of colors
n = 4   # number of vertices
graphColoring(graph, m, n)
