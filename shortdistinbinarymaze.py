from collections import deque

def shortestPath(grid, source, destination):
    
    n = len(grid)
    m = len(grid[0])
    
    sx, sy = source
    dx, dy = destination 
    
    if grid[sx][sy] == 0:
        return -1
    
    queue = deque()
    queue.append((sx, sy, 0))
    
    visited = [[False]*m for _ in range(n)]
    visited[sx][sy] = True
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    while queue:
        x, y, dist = queue.popleft()
        
        if (x, y) == (dx, dy):
            return dist
        
        for dx1, dy1 in directions:
            nx = x + dx1
            ny = y + dy1
            
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    
    return -1
grid = [
    [1,1,1,1],
    [1,1,0,1],
    [1,1,1,1],
    [0,1,0,1]
]

source = (0,0)
destination = (3,3)

print(shortestPath(grid, source, destination))