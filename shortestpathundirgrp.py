from collections import deque

def shortestPath(n, edges, src):
    # Step 1: Create adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)   # because undirected

    # Step 2: Distance array
    dist = [-1] * n
    dist[src] = 0

    # Step 3: BFS
    q = deque()
    q.append(src)

    while q:
        node = q.popleft()

        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)

    return dist
n = 6
edges = [[0,1],[0,2],[1,3],[2,4],[3,5],[4,5]]
src = 0

print(shortestPath(n, edges, src))