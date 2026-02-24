from collections import deque

def isCycleBFS(src, adj, vis):
    vis[src] = 1
    q = deque()
    
    # (node, parent)
    q.append((src, -1))
    
    while q:
        node, parent = q.popleft()
        
        for adjNode in adj[node]:
            # If not visited
            if vis[adjNode] == 0:
                vis[adjNode] = 1
                q.append((adjNode, node))
            
            # If visited and not parent -> cycle
            elif adjNode != parent:
                return True
    
    return False


def detectCycle(V, adj):
    vis = [0] * V
    
    for i in range(V):
        if vis[i] == 0:
            if isCycleBFS(i, adj, vis):
                return True
    
    return False
V = 5
adj = [
    [1,2],     # 0
    [0,2],     # 1
    [0,1,3],   # 2
    [2,4],     # 3
    [3]        # 4
]

print(detectCycle(V, adj))