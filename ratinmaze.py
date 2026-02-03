def ratInMaze(maze):
    n = len(maze)
    ans = []
    
    # visited matrix
    vis = [[0 for _ in range(n)] for _ in range(n)]
    
    # directions: Down, Left, Right, Up
    di = [1, 0, 0, -1]
    dj = [0, -1, 1, 0]
    move_char = ['D', 'L', 'R', 'U']
    
    def solve(i, j, path):
        # reached destination
        if i == n - 1 and j == n - 1:
            ans.append(path)
            return
        
        for ind in range(4):
            next_i = i + di[ind]
            next_j = j + dj[ind]
            
            # check valid move
            if (0 <= next_i < n and 0 <= next_j < n and
                maze[next_i][next_j] == 1 and vis[next_i][next_j] == 0):
                
                vis[i][j] = 1
                solve(next_i, next_j, path + move_char[ind])
                vis[i][j] = 0   # backtrack
    
    if maze[0][0] == 1:
        solve(0, 0, "")
    
    return ans
maze = [
 [1, 0, 0, 0],
 [1, 1, 0, 1],
 [1, 1, 0, 0],
 [0, 1, 1, 1]
]

print(ratInMaze(maze))
