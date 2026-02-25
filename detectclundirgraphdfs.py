def isCycleDFS(node, parent, adj, vis):
    vis[node] = 1
    
    for adjNode in adj[node]:
        # If not visited
        if vis[adjNode] == 0:
            if isCycleDFS(adjNode, node, adj, vis):
                return True
        
        # If visited and not parent -> cycle
        elif adjNode != parent:
            return True
    
    return False


def detectCycle(V, adj):
    vis = [0] * V
    
    for i in range(V):
        if vis[i] == 0:
            if isCycleDFS(i, -1, adj, vis):
                return True
    
    return False
V = 5
adj = [
    [1,2],
    [0,2],
    [0,1,3],
    [2,4],
    [3]
]

print(detectCycle(V, adj))