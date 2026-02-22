def dfs(node, adj, vis):
    vis[node] = 1
    
    for it in adj[node]:
        if not vis[it]:
            dfs(it, adj, vis)


def numProvinces(adj):
    V = len(adj)        # FIX here
    vis = [0] * V
    count = 0
    
    for i in range(V):
        if not vis[i]:
            count += 1
            dfs(i, adj, vis)
    
    return count


# Example
adj = [
    [1],
    [0],
    [3],
    [2],
    []
]

print(numProvinces(adj))