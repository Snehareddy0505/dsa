from collections import deque

def noofislands(grid):
    n = len(grid)
    m = len(grid[0])
    
    vis = [[0]*m for _ in range(n)]
    cnt = 0
    
    def bfs(row, col):
        q = deque()
        q.append((row, col))
        vis[row][col] = 1
        
        # directions: up, down, left, right
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < m:
                    if grid[nr][nc] == 1 and vis[nr][nc] == 0:
                        vis[nr][nc] = 1
                        q.append((nr, nc))
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and vis[i][j] == 0:
                bfs(i, j)
                cnt += 1
                
    return cnt
grid = [
    [1,1,0,0],
    [1,0,0,1],
    [0,0,1,1],
    [0,0,0,0]
]

print(noofislands(grid))