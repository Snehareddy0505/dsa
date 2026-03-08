def bellman_ford(V, edges, src):
    
    # Step 1: Initialize distances
    dist = [float('inf')] * V
    dist[src] = 0

    # Step 2: Relax all edges V-1 times
    for i in range(V-1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Step 3: Check for negative weight cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return

    print("Shortest distances from source:", dist)
V = 5
edges = [
    (0,1,-1),
    (0,2,4),
    (1,2,3),
    (1,3,2),
    (1,4,2),
    (3,2,5),
    (3,1,1),
    (4,3,-3)
]

bellman_ford(V, edges, 0)