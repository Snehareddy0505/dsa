def dfs(node):
    vis[node] = 1
    result.append(node)
    
    for it in adj[node]:
        if not vis[it]:
            dfs(it)

# Example graph (adjacency list)
adj = [
    [1, 2],   # 0
    [0, 3],   # 1
    [0],      # 2
    [1]       # 3
]

n = len(adj)
vis = [0] * n
result = []

dfs(0)

print(result)