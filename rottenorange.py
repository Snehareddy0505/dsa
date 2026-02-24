from collections import deque

def rottenOranges(grid):
    n = len(grid)
    m = len(grid[0])
    
    q = deque()
    vis = [[0]*m for _ in range(n)]
    
    # Step 1: Put all rotten oranges in queue
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j, 0))   # (row, col, time)
                vis[i][j] = 2
            else:
                vis[i][j] = 0
    
    tm = 0
    
    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]
    
    # Step 2: BFS
    while q:
        r, c, t = q.popleft()
        tm = max(tm, t)
        
        for i in range(4):
            nrow = r + drow[i]
            ncol = c + dcol[i]
            
            if (0 <= nrow < n and 0 <= ncol < m and
                vis[nrow][ncol] == 0 and grid[nrow][ncol] == 1):
                
                q.append((nrow, ncol, t+1))
                vis[nrow][ncol] = 2
    
    # Step 3: Check if any fresh orange left
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and vis[i][j] != 2:
                return -1
    
    return tm
grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]

print(rottenOranges(grid))