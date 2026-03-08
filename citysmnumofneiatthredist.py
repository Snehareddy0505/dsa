def findTheCity(n, edges, distanceThreshold):

    INF = float('inf')

    # Step 1: Create distance matrix
    dist = [[INF]*n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w

    # Step 2: Floyd Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Step 3: Find city with smallest neighbors
    min_count = n
    city = -1

    for i in range(n):
        count = 0
        for j in range(n):
            if i != j and dist[i][j] <= distanceThreshold:
                count += 1

        if count <= min_count:
            min_count = count
            city = i

    return city


# Example Input
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4

result = findTheCity(n, edges, distanceThreshold)

print("City with smallest neighbors:", result)