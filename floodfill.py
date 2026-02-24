from collections import deque

def floodFill(image, sr, sc, newColor):
    n = len(image)
    m = len(image[0])
    
    original = image[sr][sc]
    
    if original == newColor:
        return image
    
    q = deque()
    q.append((sr, sc))
    
    # directions
    delrow = [-1, 1, 0, 0]
    delcol = [0, 0, -1, 1]
    
    while q:
        r, c = q.popleft()
        image[r][c] = newColor
        
        for i in range(4):
            nr = r + delrow[i]
            nc = c + delcol[i]
            
            if 0 <= nr < n and 0 <= nc < m:
                if image[nr][nc] == original:
                    q.append((nr, nc))
    
    return image
image = [
 [1,1,1],
 [1,1,0],
 [1,0,1]
]

print(floodFill(image, 1, 1, 2))