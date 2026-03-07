import heapq

def minimumEffortPath(heights):
    
    rows = len(heights)
    cols = len(heights[0])
    
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = 0
    
    pq = []
    heapq.heappush(pq, (0, 0, 0))  # effort, row, col
    
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    while pq:
        effort, r, c = heapq.heappop(pq)
        
        if r == rows-1 and c == cols-1:
            return effort
        
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                
                newEffort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                
                if newEffort < dist[nr][nc]:
                    dist[nr][nc] = newEffort
                    heapq.heappush(pq, (newEffort, nr, nc))
    
    return 0
heights = [[1,2,2],
           [3,8,2],
           [5,3,5]]

print(minimumEffortPath(heights)) 