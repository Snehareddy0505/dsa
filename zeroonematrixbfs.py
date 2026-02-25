from collections import deque

def updateMatrix(mat):
    n = len(mat)
    m = len(mat[0])
    
    dist = [[0]*m for _ in range(n)]
    vis = [[0]*m for _ in range(n)]
    
    q = deque()
    
    # Step 1: Push all 0's into queue
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                q.append((i, j, 0))
                vis[i][j] = 1
    
    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]
    
    # Step 2: BFS
    while q:
        r, c, d = q.popleft()
        dist[r][c] = d
        
        for i in range(4):
            nrow = r + drow[i]
            ncol = c + dcol[i]
            
            if (0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] == 0):
                vis[nrow][ncol] = 1
                q.append((nrow, ncol, d+1))
    
    return dist
mat = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
]

print(updateMatrix(mat))