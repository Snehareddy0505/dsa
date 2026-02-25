def countDistinctIslands(grid):
    n = len(grid)
    m = len(grid[0])
    
    vis = [[0]*m for _ in range(n)]
    shapes = set()
    
    def dfs(r, c, base_r, base_c, shape):
        vis[r][c] = 1
        
        # store relative position
        shape.append((r - base_r, c - base_c))
        
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        
        for i in range(4):
            nrow = r + drow[i]
            ncol = c + dcol[i]
            
            if (0 <= nrow < n and 0 <= ncol < m and
                vis[nrow][ncol] == 0 and grid[nrow][ncol] == 1):
                
                dfs(nrow, ncol, base_r, base_c, shape)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and vis[i][j] == 0:
                shape = []
                dfs(i, j, i, j, shape)
                shapes.add(tuple(shape))   # store as tuple (hashable)
    
    return len(shapes)
grid = [
    [1,1,0,0],
    [1,0,0,0],
    [0,0,1,1],
    [0,0,1,1]
]

print(countDistinctIslands(grid)) 