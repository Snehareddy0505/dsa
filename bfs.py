from collections import deque

def bfs_graph(v, adj):
    vis = [0] * v      # visited array
    vis[0] = 1         # start from node 0
    
    q = deque()
    q.append(0)        # push starting node
    
    bfs = []           # result list
    
    while q:
        node = q.popleft()
        bfs.append(node)
        
        for it in adj[node]:
            if not vis[it]:
                vis[it] = 1
                q.append(it)
    
    return bfs
adj = [
    [1, 2],
    [0, 3],
    [0, 4],
    [1],
    [2]
]

print(bfs_graph(5, adj))
